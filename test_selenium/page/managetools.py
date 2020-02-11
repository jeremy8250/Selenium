from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage
from test_selenium.page.materials import Materials


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"
    _materials_lib_locator = (By.PARTIAL_LINK_TEXT, "素材库")

    def goto_material(self):
        self.find((self._materials_lib_locator)).click()
        return Materials(reuse=True)



