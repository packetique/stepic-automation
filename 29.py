import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, 'submit_button')
print('Button text: '+button.text)
time.sleep(5)
browser.quit()

if __name__ == '__main__':
    unittest.main()
