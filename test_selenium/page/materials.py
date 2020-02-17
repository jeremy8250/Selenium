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
        # 图片子菜单
        self.find((self._add_img_locator)).click()
        # 添加图片
        self.find((self._upload_button_locator)).send_keys(path)
        # 使用sned_keys()方法上传图片
        cancel_button = (By.LINK_TEXT, '取消')
        WebDriverWait(self._driver, 20).until(expected_conditions.invisibility_of_element_located((cancel_button)))
        # 上传时会有【取消】按钮显示
        # 等待【取消】按钮消失，再点击确定
        self.find((self._done_button_locator)).click()
        # 上传完成
        return self

    def get_img_name(self):
        img_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic')
        return self.find(img_locator).get_attribute("style")

    def remove_image(self):
        img_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic')
        remove_button_locator = (By.CSS_SELECTOR, '.ww_icon_WhiteSmallTrash')
        OK_button_locator = (By.LINK_TEXT, '确定')
        self.find(self._img_menu_locator).click()
        # 图片子菜单
        self.mouse_over_and_click(img_locator, remove_button_locator)
        self.find(OK_button_locator).click()
        return self
