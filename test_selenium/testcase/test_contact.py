from test_selenium.page.contact import Contact


class TestContact():

    def setup(self):
        self.contact = Contact(reuse=True)

    def test_add_user(self):
        pass

    def test_edit_user(self):
        self.contact.edit_user(position="测试开发")

