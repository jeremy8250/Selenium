from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, corp_name):
        self.find((By.ID, 'corp_name')).send_keys(corp_name)
        # self.driver通过初始化方法__init__从外部引入
        self.find((By.ID, 'submit_btn')).click()
        return self
        # 注册失败，返回自身

    def get_error_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            result.append(element.text)
        return result
