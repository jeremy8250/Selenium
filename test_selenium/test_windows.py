from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindows:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/topics/21805")

    def test_frame(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '第六届中国互联网测试开发大会').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '演讲申请').click()

    def teardown(self):
        sleep(3)
        self.driver.quit()
