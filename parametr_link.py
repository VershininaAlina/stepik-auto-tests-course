import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMStep():
    @pytest.mark.parametrize('step', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
    def test_guest_should_see_login_link(self, browser: WebDriver, step: str, ids, limks):
        link = f"https://stepik.org/lesson/{step}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        input1= browser.find_element_by_css_selector("textarea.ember-text-area")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        browser.implicitly_wait(5)
        but = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission' )))
        but.click()
        result_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text
        assert result_text != "Correct!"
        print("12Current result is: " + result_text)
            

