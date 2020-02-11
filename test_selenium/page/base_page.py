from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # BasePage存放通用方法，其他页面可以直接继承BasePage

    _base_url = ""
    # 初始化_base_url为空，这样不用每个页面都需要加_base_url
    _driver = None
    # _driver为内部变量，只有初始化的时候声明为None，后面才能被正确调用
    def __init__(self, driver: WebDriver = None, reuse=False):
        # reuse:是否复用已有的浏览器进程
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # _driver:隐藏driver,让外部不可调用
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # login与register的页面需要用这个方法
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
            # 允许每个类初始化的时候打开自己定义的地址

    def find(self, locator):
        return self._driver.find_element(*locator)

    def close(self):
        self._driver.quit()
