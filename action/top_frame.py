import common
from time import sleep


def modify_password(driver):
    driver.find_element_by_xpath('//span[@onclick="PersonCenter()"]').click()
    sleep(1)
    driver.switch_to.default_content()
    driver.switch_to.frame('ResetPassword')
    driver.find_element_by_id('txtOldPass').send_keys('wnxy123456')
    driver.find_element_by_id('txtNewPass').send_keys('wnxy123456')
    driver.find_element_by_id('txtConfirmPass').send_keys('wnxy123456')
    driver.find_element_by_id('btnEditPassword').click()
    sleep(1)


def secure_quit(driver):
    driver.find_element_by_xpath('//span[@onclick="IndexOutHiLink();"]').click()
    driver.switch_to.default_content()
    driver.switch_to.frame('confirmDialog')
    driver.find_element_by_id('Button1').click()
    sleep(1)
