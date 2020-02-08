from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import calculate

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element_by_id('book').click()
    x = driver.find_element_by_id('input_value').text
    driver.find_element_by_id('answer').send_keys(calculate.calc(x))
    driver.find_element_by_id('solve').click()
    time.sleep(5)

finally:
    driver.quit()