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
    chal_txt = driver.find_element(By.ID,'challenge').text
    parts = chal_txt.split()
    a = int(parts[2])
    b = int(parts[4].replace('?',''))
    cur_a = a+b
    answ_select = Select(driver.find_element(By.ID,'answerSelect'))
    answ_select.select_by_value(str(cur_a))
    time.sleep(1)
    driver.find_element(By.ID,'submitBtn').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
