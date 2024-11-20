#Существуют ситуации, когда базового выполнения недостаточно, порой надо выполнить доп действия на страница сайта , через скрипты на JavaScript Чтобы эти скрипты выполнялись используется метод Execute_script

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
    driver.get('https://erikdark.github.io/QA_autotests_09/')

    # ниже пишем свой код
    driver.execute_script('alert("hello")')
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()


