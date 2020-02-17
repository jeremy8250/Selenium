from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # BasePage存放通用方法，其他页面可以直接继承BasePage

    _base_url = ""
    # 初始化_base_url为空，这样不用每个页面都需要加_base_url
    # 类变量

    _driver = None
    # _driver:隐藏driver,让外部不可调用
    # _driver为内部变量，只有当初始化的时候声明为None，后面才能被正确调用

    def __init__(self, driver: WebDriver = None, reuse=False):
        # reuse:是否复用已有的浏览器进程
        if driver is None:
        # 如果没有chromedriver,就按照下面的方法给一个
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
                # 如果page页reuse=true，则复用当前的chrome浏览器
            else:
                self._driver = webdriver.Chrome()
                # 如果page页reuse=false，则起一个新的浏览器进程
        else:
            self._driver = driver
            # login与register的页面需要用这个方法

        if self._base_url != "":
            self._driver.get(self._base_url)
            # 允许每个类初始化的时候打开自己定义的地址
            # page页中的_base_url会覆盖basepage中的_base_url,使这段代码生效

        self._driver.implicitly_wait(3)
        # 隐式等待

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
            # *by作用:解析page页中定义为元组类型的定位符
        else:
            return self._driver.find_element(by, locator)

    def mouse_over_and_click(self, locator1, locator2):
        # 鼠标悬停在元素1上，待元素2出现后再点击
        ac = ActionChains(self._driver)
        return ac.move_to_element(self.find(locator1)).move_to_element(self.find(locator2)).click().perform()

    def close(self):
        self._driver.quit()
