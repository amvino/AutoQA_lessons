import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_08/')

    # ниже пишем свой код
    driver.find_element(By.CSS_SELECTOR,'.container select').click()
    driver.find_element(By.CSS_SELECTOR,'.container option:nth-child(3)').click()
    driver.find_element(By.CSS_SELECTOR,'.container-main select').click()
    driver.find_element(By.CSS_SELECTOR,'.container-main [value="3"]').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
