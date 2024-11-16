#Для переключения на новую вкладку, надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window
#Чтобы указать имя новой вкладки, нужно использовать метод window_handles, который по сути возвращает массив имен всех вкладок.
#Также мы можем запомнить нашу изначальную вкладку чтобы перейти на нее.
#    driver.switch_to.window(window_name)
#    2 вкалдка
#    new_window = driver.window_handles[1]
#    1 вкалдка
#    first_window = driver.window_handles[0]

#Решение:

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
    driver.get('https://erikdark.github.io/QA_autotests_13/')

    # ниже пишем свой код
    driver.find_element(By.ID,'openNewPageBtn').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID,'displayTextBtn').click()

    if driver.find_element(By.ID,'displayText').text == 'Я СДЕЛАЛ':
        print('da')
    else:
        print('nope')   
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()