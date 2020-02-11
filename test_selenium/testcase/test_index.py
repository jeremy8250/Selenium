from test_selenium.page.index import Index


class TestIndex:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register('abc')

    def test_login(self):
        regitser_page = self.index.goto_login().goto_registry().register('efg')
        assert '请选择' in "|".join(regitser_page.get_error_message())
        # 转成以|拼接的列表

    def teardown(self):
        self.index.close()
