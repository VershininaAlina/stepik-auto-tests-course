from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure")
    x_valuex = x_element.get_attribute("valuex")

    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = x_valuex
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("body > div > form > div > div > button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 