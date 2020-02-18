from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/topics/21495")

    def test_frame(self):
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, '.ant-btn.published-form__submit.sc-htpNat.hyXsOZ.ant-btn-primary')

    def teardown(self):
        sleep(3)
        self.driver.quit()
