from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('http://suninjuly.github.io/wait1.html')
    driver.find_element_by_id('verify').click()
    message = driver.find_element_by_id('verify_message')
    print(message.text)
    assert "successful" in message.text
finally:
    driver.quit()
