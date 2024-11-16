#Загрузка файлов через селениум.
#Допустим есть форма, туда надо загрузить файл.
#Все что надо, это по сути найти  элемент и через send_keys вставить его туда.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_11/')

    # ниже пишем свой код   
    #путь к файлу
    img_path = r'C:\Users\атек\Desktop\python_cource\my_tests\img.jpg'

    driver.find_element(By.ID,'imageInput').send_keys(img_path)
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()