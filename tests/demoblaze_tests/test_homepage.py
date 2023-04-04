import pytest
import allure
from allure_commons.types import AttachmentType

from pages.demoblaze.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page of Demoblaze has correct title")
    def test_homepage_title(self):
        homepage = HomePage(self.driver)
        homepage.open()
        assert ("STORE" in homepage.get_page_title())
        allure.attach(self.driver.get_screenshot_as_png(), name="home_results", attachment_type=AttachmentType.PNG)

