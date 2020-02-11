from test_selenium.page.managetools import ManageTools


class TestManageTools:

    def setup(self):
        self.managetools = ManageTools(reuse=True)

    def test_upload_images(self):
        self.managetools.goto_material().upload_images("/Users/ouchou/Projects/Selenium/test_selenium/data/douyin.jpg")