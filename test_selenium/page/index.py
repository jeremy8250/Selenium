from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"  # index的地址

    def goto_register(self):
        self.find((By.PARTIAL_LINK_TEXT, '立即注册')).click()
        # self.driver通过初始化方法__init__从外部引入
        return Register(self._driver)

    def goto_login(self):
        self.find((By.LINK_TEXT, '企业登录')).click()
        return Login(self._driver)