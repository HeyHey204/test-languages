import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestParams():
    def test_params(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(10)

        time.sleep(5)
        button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))

        assert button != False, "Where is my button?"

        print("--Button exist--")
