from test_selenium.page.managetools import ManageTools


class TestManageTools:

    def setup(self):
        self.managetools = ManageTools(reuse=True)

    def test_upload_images(self):
        self.managetools.goto_material().upload_images("/Users/ouchou/Projects/Selenium/test_selenium/data/douyin.jpg")
        assert "douyin.jpg" in self.managetools.goto_material().get_img_name()

    def test_remove_imgs(self):
        self.managetools.goto_material().remove_image()