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
    driver.get('https://erikdark.github.io/QA_autotests_08/')

    # ниже пишем свой код
    select =  Select(driver.find_element(By.CSS_SELECTOR,'.container select'))   
    select.select_by_value('3')
    select_2  = Select(driver.find_element(By.CSS_SELECTOR,'.container-main select'))
    select_2.select_by_value('2')
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()