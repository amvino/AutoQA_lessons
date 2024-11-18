#1. Успешная регистрация: Заполнить все поля формы (имя пользователя, email, пароль). Нажать кнопку "Зарегистрироваться". Убедиться, что появилось сообщение "Вы успешно зарегистрированы!".
#2. Ошибка при незаполненных полях: Оставить все поля пустыми. Нажать кнопку "Зарегистрироваться". Убедиться, что появилось сообщение "Пожалуйста, заполните все поля.".
#3. Ошибка при незаполненном имени пользователя: Оставить поле "Имя пользователя" пустым. Заполнить поля "Email" и "Пароль". Нажать кнопку "Зарегистрироваться". Убедиться, что появилось сообщение "Пожалуйста, заполните все поля.".
#4. Ошибка при незаполненном email: Оставить поле "Email" пустым. Заполнить поля "Имя пользователя" и "Пароль". Нажать кнопку "Зарегистрироваться". Убедиться, что появилось сообщение "Пожалуйста, заполните все поля.".
#5.Ошибка при незаполненном пароле: Оставить поле "Пароль" пустым. Заполнить поля "Имя пользователя" и "Email". Нажать кнопку "Зарегистрироваться". Убедиться, что появилось сообщение "Пожалуйста, заполните все поля.".

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_reg():

    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')

    try:
        #1
        test_succesful_reg(driver)
        #2
        test_empty_username_error(driver)

    finally:
        time.sleep(3)
        driver.quit()


def test_succesful_reg(driver):

    driver.find_element(By.ID,'username').send_keys('testuser')
    driver.find_element(By.ID,'email').send_keys('testuser@example.com')
    driver.find_element(By.ID,'password').send_keys('testuserpassword')
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'success-message')))

    assert driver.find_element(By.ID,'success-message').text == 'Вы успешно зарегистрированы!'


def test_empty_username_error(driver):

    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
    driver.find_element(By.ID,'username').clear()
    driver.find_element(By.ID,'email').clear()
    driver.find_element(By.ID,'password').clear()
   
    # driver.find_element(By.ID,'username').send_keys('testuser')
    driver.find_element(By.ID,'email').send_keys('testuser@example.com')
    driver.find_element(By.ID,'password').send_keys('testuserpassword')
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input:invalid')))

    error_message  = driver.execute_script("""
        const usernameField = document.getElementById('username');
        return usernameField.validationMessage;
    """)
    assert   error_message
