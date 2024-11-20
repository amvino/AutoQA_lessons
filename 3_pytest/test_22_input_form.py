#Есть форма, есть поле в котором мы считываем введенный текст, грубо говоря написать автотест, на ввод данных и проверку, что введенные данные и исходные ==.  https://erikdark.github.io/QA_autotest_stop_list/

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():

    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotest_stop_list/')

    try:
        input_text = 'Привет, Sir'
        driver.find_element(By.ID,'inputField').send_keys(input_text)
        driver.find_element(By.ID,'submitButton').click()

        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,'result'),input_text))

        assert input_text in driver.find_element(By.ID,'result').text
   
    finally:
        # time.sleep(3)
        driver.quit()