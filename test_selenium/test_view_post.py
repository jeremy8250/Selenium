import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDefaultSuite:
    def setup_method(self):
        browser = os.getenv("browser", "").lower()
        if browser == "headless":
            self.driver = webdriver.PhantomsJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1280,1696")

            options.debugger_address="127.0.0.1:9222"
        # self.driver = webdriver.Chrome()  # 初始化driver
        self.driver = webdriver.Chrome(options=options) # headless模式
        self.driver.get("https://testerhome.com/")  # 打开网址
        # self.driver.set_window_size(1680, 954) # headless模式下需要注释掉

        self.driver.implicitly_wait(6)  # 隐式等待

    def teardown_method(self):
        # time.sleep(5)
        self.driver.quit()

    def test_post(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '社团').click()
        element = (By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]')  # 定义element为元组
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()  # class=topic下面的第一个节点下面的title,下面的a链接
