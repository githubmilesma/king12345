import unittest
from time import sleep

import common
from action import top_frame
from selenium.webdriver.common.by import By


class TopFrame(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = common.get_driver()
        common.login_with_cookies(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        common.quit_driver(cls.driver)

    def setUp(self) -> None:
        self.driver.switch_to.frame('tabs_iframe_ITop')

    def tearDown(self) -> None:
        self.driver.refresh()
        sleep(1)

    @classmethod
    @unittest.skip('skip')
    def test_return_homepage(cls):
        cls.driver.find_element_by_xpath('//span[@onclick="Replace()"]').click()
        sleep(1)

    @classmethod
    def test_modify_password(cls):
        # 修改密码操作
        top_frame.modify_password(cls.driver)
        # 弹出修改成功确认
        common.accept_alert(cls.driver)
        # 切换默认frame
        cls.driver.switch_to.default_content()
        sleep(1)
        # 判断修改密码的frame应该不存在
        present = common.is_present(cls.driver, By.ID, 'ResetPassword')
        cls.assertFalse(cls(), present)

    @classmethod
    def test_secure_quit(cls):
        # 安全退出操作
        top_frame.secure_quit(cls.driver)
        # 断言
        present = common.is_present(cls.driver, By.ID, 'tbxUserId')
        cls.assertTrue(cls(), present)


if __name__ == '__main__':
    unittest.main(verbosity=2)
