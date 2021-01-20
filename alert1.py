from selenium import webdriver
import time
import os 
import math
def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()

  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 
