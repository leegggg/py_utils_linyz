from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


def blockFindByXpath(driver: webdriver, xpath, retry=200) -> WebElement:
    tag = None
    for _ in range(retry):
        try:
            tag = driver.find_element_by_xpath(xpath)
        except Exception:
            pass
        if tag:
            break
        sleep(0.1)
    sleep(0.1)
    return tag
