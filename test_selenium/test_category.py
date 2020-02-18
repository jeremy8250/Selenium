import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCategory:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(6)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_category(self):
        post = self.driver.find_element(By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]')
        if post:
            post.click()
            self.driver.find_element(By.CSS_SELECTOR, 'button[data-toggle="dropdown"]').click()
            self.driver.find_element(By.CSS_SELECTOR, '.toc-item.toc-level-2:nth-child(4) a').click()
        else:
            print("post not found!")

