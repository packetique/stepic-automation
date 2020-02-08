from selenium import webdriver


try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get("http://suninjuly.github.io/wait2.html")

    button = driver.find_element_by_id("verify")
    button.click()
    message = driver.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    driver.quit()