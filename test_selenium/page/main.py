from selenium.webdriver.common.by import By

from page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 覆盖父类的_base_url,使之不为空

    def download(self):
        pass

    def import_user(self, path):
        self.find((By.PARTIAL_LINK_TEXT, '导入通讯录')).click()
        self.find((By.ID, 'js_upload_file_input')).send_keys(path)
        self.find((By.LINK_TEXT, '导入')).click()
        self.find((By.CSS_SELECTOR, '.ww_flatSwitch_slider')).click()
        self.find((By.LINK_TEXT, '完成')).click()
        return self

    def goto_contact(self):
        contact_locator = (By.LINK_TEXT, '通讯录')
        self.find(contact_locator).click()
        return Contact(reuse=True)

    def add_member(self):
        add_number_locator = (By.LINK_TEXT, '添加成员')
        # 元素类型为元组
        # 方法变量
        self.find(add_number_locator).click()
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        # 使用execute_script方法可以在网页缩放非100%时，仍然实现元素点击
        return Contact(reuse=True)

    def send_message(self):
        locator = (By.LINK_TEXT, '消息群发')
        self.find(locator).click()
        return Message(reuse=True)

