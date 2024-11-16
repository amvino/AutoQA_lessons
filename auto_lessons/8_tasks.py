#Задача: https://erikdark.github.io/Qa_autotests_06/
#Решение:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/Qa_autotests_06/')

    # ниже пишем свой код   
    chel_element = driver.find_element(By.ID,'challenge')
    a = int(chel_element.get_attribute('data-a'))
    b = int(chel_element.get_attribute('data-b'))
    corr_sum = a+b

    driver.find_element(By.ID,'answer').send_keys(corr_sum)
    driver.find_element(By.ID,'notRobot').click()
    driver.find_element(By.ID,'cool').click()
    driver.find_element(By.ID,'submitBtn').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()


#Задача: https://erikdark.github.io/Qa_autotest_07/
#Решение:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/Qa_autotest_07/')

    # ниже пишем свой код   
    chel_el = driver.find_element(By.ID,'challenge')
    parts = chel_el.text.split()

    a = int(parts[2])
    img_el = driver.find_element(By.ID,'numberImage')

    b = int(img_el.get_attribute('data-b'))
    cor_a = a+b

    driver.find_element(By.ID,'answer').send_keys(cor_a)
    driver.find_element(By.ID,'submitBtn').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()