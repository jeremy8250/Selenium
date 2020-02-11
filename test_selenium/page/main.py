from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        pass

    def import_user(self, path):
        self.find((By.PARTIAL_LINK_TEXT, '导入通讯录')).click()
        self.find((By.ID, 'js_upload_file_input')).send_keys(path)
        self.find((By.LINK_TEXT, '导入')).click()
        self.find((By.CSS_SELECTOR, '.ww_flatSwitch_slider')).click()
        self.find((By.LINK_TEXT, '完成')).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return self

    def add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        # 使用execute_script方法可以在网页缩放非100%时，仍然实现元素点击
        return Contact(reuse=True)

    def send_message(self):
        locator = (By.LINK_TEXT, '消息群发')
        self.find(locator).click()
        return Message(reuse=True)

