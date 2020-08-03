import requests
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pathlib import Path
import re

with requests.Session() as req:
    USER_AGENT_UC_FF_59_WIN = \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
    REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': USER_AGENT_UC_FF_59_WIN
    }
    req.proxies = {
        'https': 'http://192.168.200.1:7890',
        'http': 'http://192.168.200.1:7890'
    }
    req.headers = REQUEST_HEADERS

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': 'http://192.168.200.1:7890',
    'noProxy': ''
})

dataBasePath = Path('data')
cookiesPath = dataBasePath.joinpath('cookies.json')
bookListPath = dataBasePath.joinpath('books.json')
PROFILE_PATH = Path('C:/Users/yizho/AppData/Roaming/Mozilla/Firefox/Profiles/h6llh6y6.baiduyun')
outputBase: Path = dataBasePath.joinpath('books')
TEMPDIR = dataBasePath.joinpath('temp')
TEMP_EPUB_EXT = TEMPDIR.joinpath('epub')
infoLinkRegexp = re.compile(r"https://kindleer.com/([^/\\%]+).html")
BAIDU_YUN_REGEXP = re.compile(r"https?://pan.baidu.com/s/([a-zA-Z0-9_\-]+)")
BAIDU_YUN_FORMAT = "https://pan.baidu.com/s/{}"
BAIDU_YUN_SAVE_LOG = dataBasePath.joinpath('baiduyun_log.json')
BAIDU_YUN_SEC_REGEXP = re.compile(r"提取码[：:] ?([0-9a-z]{4})")
BAIDU_YUN_DATA_PATH = Path("data/baiduyun")
BAIDU_YUN_LOG_FILE_NAME = "baidu_log.json"
