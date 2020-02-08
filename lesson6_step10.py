from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys("Constantine")
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys("Fr0ZT")
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys("newkosss@gmail.com")
    input4 = browser.find_element_by_css_selector('.second_block .first')
    input4.send_keys("102")
    input4 = browser.find_element_by_css_selector('.second_block .second')
    input4.send_keys("Odessa")
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
