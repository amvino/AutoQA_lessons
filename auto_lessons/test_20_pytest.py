#Задание:
#Сделать 2 проверки
#1.assert на то что кнопка стала доступной
#2.assert на то что текст сообщения совпадает с ожидаемым.

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_your_name_1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/Qa_autotest_15/')

        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.ID,'verify')))

        assert driver.find_element(By.ID,'verify').is_enabled(), 'кнопка должна стать доступной'

        driver.find_element(By.ID,'verify').click()

        WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.ID,'verify_message')))

        assert driver.find_element(By.ID,'verify_message').text == 'Verification successful!','текст должен быть Verification successful!'

    finally:
        time.sleep(3)
        driver.quit()