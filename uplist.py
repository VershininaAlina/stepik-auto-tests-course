from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
def calc(x,y):
     return str(int(x)+int(y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("select").click()
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    result = calc(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()