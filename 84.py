from selenium import webdriver
import time
import pytest
import math

phrase = ''
links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_link(browser, link):
    browser.get(link)
    time.sleep(4)
    answer = math.log(int(time.time()))
    browser.find_element_by_tag_name('textarea').send_keys(str(answer))
    browser.find_element_by_tag_name('button').click()
    time.sleep(2)
    result = browser.find_element_by_tag_name('pre').text
    assert result == 'Correct!', f"{result}"






