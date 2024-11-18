#Проверка 3 сценариев что появляется текст с успехом и алерт с неуспехом 
#логин testuser
#pw password123

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_suc_login():

    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')

    try:
        driver.find_element(By.ID,'openModalButton').click()

        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'loginModal')))

        driver.find_element(By.ID,'username').send_keys('testuser')
        driver.find_element(By.ID,'password').send_keys('password123')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

        WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,'loginModal')))
       
        assert not driver.find_element(By.ID,'loginModal').is_displayed()

    finally:
        driver.quit()