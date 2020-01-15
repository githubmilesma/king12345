import traceback
from datetime import datetime
from miles.tools import *
from time import sleep
from os import path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def accept_alert(driver):
    try:
        driver.switch_to.alert.accept()
    except Exception:
        error = traceback.format_exc()
        with open('error.log', 'a+')as f:
            f.write(str(datetime.now()).split('.')[0] + '\t' + error)


def click(ele):
    sleep(1)
    ele.click()


def is_present(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    return True


def login_with_cookies(driver):
    cur_path = 'D:/projects/king12345/cookies.txt'
    with open(cur_path) as f:
        content = f.read()
    data = OtherTools.source_to_dict(content)
    driver.get('http://xxx.xx.xxx.xx:xxxx/WorkLogin.aspx')
    sleep(1)
    accept_alert(driver)

    for key, value in zip(data, data.values()):
        driver.add_cookie({'name': key, 'value': value})
    driver.get('http://xxx.xx.xxx.xx:xxxx/IndexMenu.aspx')
    sleep(1)
    accept_alert(driver)


def quit_driver(driver):
    driver.quit()


if __name__ == '__main__':
    driver = get_driver()
    login_with_cookies(driver)
    quit_driver(driver)
