import random
from datetime import datetime

import yaml
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    _rand_num = random.randint(10000000, 99999999)  # 8位随机整数
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    # todo: yaml数据驱动

    def add_member(self):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '[name = "gender"][value = "2"]')
        arrow_locator = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input_arrowWrap')
        zipcode_locator = (By.CSS_SELECTOR, '[data-value = "86"]')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR, 'form.js_member_editor_form div:nth-child(3) a.js_btn_save')
        self.find((name_locator)).send_keys("测开" + str(self._rand_num))
        self.find((acctid_locator)).send_keys("ACCT" + str(self._rand_num))
        self.find((gender_locator)).click()
        self.find((arrow_locator)).click()
        self.find((zipcode_locator)).click()
        self.find((mobile_locator)).send_keys("138" + str(self._rand_num))
        self.find((save_locator)).click()
        return self

    def edit_user(self, position=""):
        self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr_Inactive')[0].click()
        self.find((By.LINK_TEXT, '编辑')).click()
        element = self.find((By.CSS_SELECTOR, '[name="position"]'))
        element.clear()
        element.send_keys(position + str(datetime.now()))
        self.find((By.LINK_TEXT, '保存')).click()
        return self
