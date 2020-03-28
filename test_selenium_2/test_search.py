from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSearch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com')

        self.driver.implicitly_wait(6)

    def test_search(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="q"]').send_keys("appium")
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="q"]').send_keys(Keys.ENTER)


    def teardown(self):
        sleep(3)
        self.driver.quit()
