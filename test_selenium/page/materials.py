import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class Materials(BasePage):
    _img_menu_locator = (By.LINK_TEXT, '图片')
    _add_img_locator = (By.LINK_TEXT, '添加图片')
    _upload_button_locator = (By.CSS_SELECTOR, '.material_upload_input')
    _done_button_locator = (By.CSS_SELECTOR, '[d_ck="submit"]')

    def upload_images(self, path):

        self.find((self._img_menu_locator)).click()
        self.find((self._add_img_locator)).click()
        self.find((self._upload_button_locator)).send_keys(path)
        cancel_button = (By.LINK_TEXT, '取消')
        WebDriverWait(self._driver, 20).until(expected_conditions.invisibility_of_element_located((cancel_button)))
        # 显示等待取消按钮消失，再点击确定
        self.find((self._done_button_locator)).click()
        return self