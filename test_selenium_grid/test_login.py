from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def setup(self):
        chrome_capabilities = {
            "browserName": "chrome",
            "platform": "ANY",
        }
        self.driver = webdriver.Remote("http://192.168.1.9:4444/wd/hub", chrome_capabilities)
        # self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(3)

    def test_testerhome_login(self):
        self.driver.find_element(By.LINK_TEXT, "登录").click()

    def teardown(self):
        self.driver.quit()
