import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestParams():
    def test_params(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        button = browser.find_elements_by_css_selector(
            ".btn-add-to-basket")

        assert button, "\n---Where is my button?!---"
