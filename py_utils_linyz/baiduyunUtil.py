# py_utils_linyz.baiduyunUtil

import json
from py_utils_linyz.seleniumUtils import blockFindByXpath
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .common import BAIDU_YUN_DATA_PATH, BAIDU_YUN_FORMAT, BAIDU_YUN_LOG_FILE_NAME
from .common import BAIDU_YUN_REGEXP, BAIDU_YUN_SEC_REGEXP, PROFILE_PATH
import re
from datetime import datetime
from pathlib import Path


class NonBaiduYunUrlException(Exception):
    pass


def findBaiduYunSec(txt):
    sec = None
    match = re.compile(r"百度提取码[：:] ?([0-9a-z]{4})").search(txt)
    if match:
        sec = match.groups()[0]
        return sec
    match = BAIDU_YUN_SEC_REGEXP.search(txt)
    if match:
        sec = match.groups()[0]
        return sec
    match = re.compile("[^a-z0-9]([a-z0-9]{4})[^a-z0-9]").search(txt)
    if match:
        sec = match.groups()[0]
        return sec
    return sec


def decodeBaiduYunUrl(url) -> str:
    match = BAIDU_YUN_REGEXP.search(url)
    if not match:
        return None
    return match.groups()[0]


def makeBaiduUrl(index) -> str:
    return BAIDU_YUN_FORMAT.format(index)


def loadLog(logPath: Path):
    log = {}
    try:
        with open(logPath, encoding='utf-8') as fp:
            log = json.load(fp)
    except Exception:
        pass
    if not log.get('log'):
        log['log'] = []
    return log


def updateLog(log: dict, status: str, href: str, title: str):
    log['status'] = status
    if not log.get('log'):
        log['log'] = []
    log['log'].append({
        'mod_date': datetime.now().isoformat(),
        'status': status,
        'href': href,
        'title': title
    })
    return log


def saveLog(path: Path, log):
    os.makedirs(path.parent, exist_ok=True)
    log['mod_date'] = datetime.now().isoformat()
    with open(path, 'w', encoding='utf-8') as basicInfoJson:
        json.dump(log, basicInfoJson, ensure_ascii=False, indent=4)


class BaiduYunUtil():
    def __init__(
            self,
            firefoxProfilePath=str(PROFILE_PATH),
            tempDirKeyWord="00000asedsswdfs",
            uuidKeyWord="0000UUIDaawdsasswvf",
            secInputId="ts8E18",
            selectAllId="zbyDdwb",
            logPath=BAIDU_YUN_DATA_PATH):

        fp = webdriver.FirefoxProfile(firefoxProfilePath)
        self.firefox: webdriver = webdriver.Firefox(firefox_profile=fp)
        self.tempDirKeyWord = tempDirKeyWord
        self.uuidKeyWord = uuidKeyWord
        self.secInputId = secInputId
        self.selectAllId = selectAllId
        self.logPath: Path = logPath
        os.makedirs(logPath, exist_ok=True)
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.firefox.quit()

    def saveLog(self, path: Path, log: dict, status: str, show=False):
        if show:
            print(status, end=" ")
        log = updateLog(
            log=log,
            status=status,
            href=self.firefox.current_url,
            title=self.firefox.title)
        saveLog(path, log)

    def saveToBaiduYun(self, index: str, sec: str, show=False, skipOk=True, skipDead=True, skipSecError=True):
        url = makeBaiduUrl(index)
        dataDir = self.logPath.joinpath(index)
        os.makedirs(dataDir, exist_ok=True)
        logPath = dataDir.joinpath(BAIDU_YUN_LOG_FILE_NAME)
        log = loadLog(logPath)
        '//*[@id="ayujnLQ"]'

        if skipOk and log.get('status') == 'ok':
            if show:
                print("Already done", end=" ")
            return log
        if skipDead and log.get('status') == 'dead':
            if show:
                print("Dead link", end=" ")
            return log
        if skipSecError and log.get('status') == 'sec_error':
            if show:
                print("Sec is not correct", end=" ")
            return log

        self.firefox.get(url)
        self.saveLog(logPath, log, 'open', show)

        secInput = None
        try:
            # secInput = self.firefox.find_element_by_id(self.secInputId)
            secInput = self.firefox.find_element_by_xpath(
                '//dl[contains(@class, "pickpw")]/dd[contains(@class, "input-area")]/input')
        except Exception:
            pass
        if not secInput:
            self.saveLog(logPath, log, 'dead', show)
            return log

        secInput.send_keys(sec)
        secInput.send_keys(Keys.ENTER)
        self.saveLog(logPath, log, 'open_url', show)

        saveSpan = blockFindByXpath(self.firefox, "//span[contains(text(),'保存到网盘')]", 50)
        if not saveSpan:
            if blockFindByXpath(self.firefox, "//div[contains(text(),'提取码错误')]", 50):
                self.saveLog(logPath, log, 'sec_error', show)
                if not saveSpan:
                    return log

        if not saveSpan:
            saveSpan = blockFindByXpath(self.firefox, "//span[contains(text(),'保存到网盘')]", 200)
            self.saveLog(logPath, log, 'wait_open', show)

        if not saveSpan:
            return log

        # Select All
        try:
            selectAllDiv = self.firefox.find_element_by_class_name(self.selectAllId)
            selectAllDiv.click()
            self.saveLog(logPath, log, 'selected_all', show)
        except Exception:
            pass

        targetDiv = None
        try:
            for _ in range(20):
                if targetDiv:
                    break
                saveSpan.click()
                self.saveLog(logPath, log, 'click_open', show)
                targetDiv = blockFindByXpath(
                    self.firefox, "//span[contains(text(),'{}')]".format(self.tempDirKeyWord), 10)
        except Exception:
            pass

        try:
            targetDiv.click()
            blockFindByXpath(self.firefox, "//span[contains(text(),'{}')]".format(self.uuidKeyWord), 200)
            self.saveLog(logPath, log, 'find_target', show)
            newDirInput = None
            for _ in range(20):
                newDirA = blockFindByXpath(self.firefox, "//a[contains(@title, '新建文件夹')]")
                newDirA.click()
                self.saveLog(logPath, log, 'new_dir', show)
                newDirInput = blockFindByXpath(self.firefox, "//input[contains(@value, '新建文件夹')]", 10)
                if newDirInput:
                    break
            newDirInput.send_keys(index)
            newDirInput.send_keys(Keys.ENTER)
            self.saveLog(logPath, log, 'new_dir_info', show)
            blockFindByXpath(self.firefox, "//span[contains(text(),'{}')]".format(index))
            self.saveLog(logPath, log, 'new_dir_check', show)
            okBtn = blockFindByXpath(self.firefox, "//a[contains(@title, '确定')]")
            okBtn.click()
            self.saveLog(logPath, log, 'saving', show)
            succSpan = blockFindByXpath(self.firefox, "//span[contains(text(),'尊贵的超级会员，已为您成功保存文件')]")
            if succSpan:
                self.saveLog(logPath, log, 'ok', show)
            else:
                self.saveLog(logPath, log, 'save_failed', show)
        except Exception:
            pass
        return log


if __name__ == "__main__":
    client = BaiduYunUtil()
    client.saveToBaiduYun('1MWmWW2V0aZpfbp1–fSm8Q', '21tj')
    client.firefox.quit()
