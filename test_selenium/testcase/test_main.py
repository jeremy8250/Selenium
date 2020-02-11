from test_selenium.page.main import Main


class TestMain:

    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member()
        # assert "aaa" in self.main.get_message()

    def test_import_user(self):
        self.main.import_user("/Users/ouchou/Projects/Selenium/test_selenium/data/通讯录批量导入模板.xlsx")
        # assert "success" in self.main.get_message()

    def test_send_message(self):
        message = self.main.send_message()
        message.send(app="测开十一期", content="this is a demo", group="十一")
        # assert "content" in message.get_history()