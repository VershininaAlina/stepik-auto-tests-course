from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    input1.send_keys("Alina")
    input2 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
    input2.send_keys("Vershinina")
    input3 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
    input3.send_keys("Kirillastrovgmail.com")
    import os 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  
    input4 = browser.find_element_by_css_selector("#file")
    input4.send_keys(file_path)
  
  
   
    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 
