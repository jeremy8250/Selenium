import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork:

    def setup(self):
        # 思寒
        options = webdriver.ChromeOptions
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)  # 复用浏览器，不弹出新的浏览器
        # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

        # # 若桐
        # chromeOptions = Options()
        # chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # self.driver = webdriver.Chrome(options=chromeOptions)
        # # Chrome --remote-debugging-port=9222


        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开网址

        """
        变量赋值
        """
        self.member = (By.CSS_SELECTOR, '.js_has_member > div:nth-child(1) > a.js_add_member')
        self.department = (By.CSS_SELECTOR, '.multiPickerDlg_left_cnt_list li[role="treeitem"]:nth-child(2) div')
        self.rand_num = random.randint(10000000, 99999999)  # 8位随机整数
        self.name = "测开" + str(self.rand_num)
        self.account = "tester" + str(self.rand_num)
        self.mobile = '138' + str(self.rand_num)

        self.driver.implicitly_wait(6)  # 隐式等待6秒

    def wait(self, timeout, method):
        return WebDriverWait(self.driver, timeout).until(method)

    def get_name(self):
        for names in [
            'return document.querySelector("#member_list tr:nth-child(1) td.member_colRight_memberTable_td:nth-child(2)").title']:
            name = self.driver.execute_script(names)
            return name

    def get_mobile(self):
        for mobiles in [
            'return document.querySelector("#member_list tr:nth-child(1) td.member_colRight_memberTable_td:nth-child(5)").title']:
            mobile = self.driver.execute_script(mobiles)
            return mobile

    """
    测试用例：添加成员并保存
    """

    def test_we_work(self):
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        self.wait(10, ec.element_to_be_clickable((self.member)))
        self.driver.find_element(*self.member).click()  # 添加成员
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(self.name)  # 姓名
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(self.account)  # 账号
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(self.mobile)  # 手机
        self.driver.find_element(By.CSS_SELECTOR, '.ww_groupSelBtn_add.js_show_party_selector').click()  # 修改部门
        self.wait(10, ec.element_to_be_clickable(self.department))  # 等待部门弹窗出现
        self.driver.find_element(*self.department).click()  # 选择部门
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.member_mainParty_dialog .ww_dialog_foot a[d_ck="submit"]').click()  # 确认
        self.driver.find_element(By.CSS_SELECTOR, '.ww_checkbox[name=sendInvite]').click()  # 取消发送邀请
        self.driver.find_element(By.CSS_SELECTOR,
                                 'form.js_member_editor_form div:nth-child(3) a.js_btn_save').click()  # 保存

    def teardown(self):
        self.driver.quit()
