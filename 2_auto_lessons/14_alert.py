# просто alert(): driver.switch_to.alert.accept()
#У него только 1 действие - принять
#Чтобы его принять надо на него переключится, с помощью switch_to.alert
#Если вам нужен текст из alert то вы пишите .text

# Есть confirm() - у него 2 кнопки ( согласен, отмена)
#Тоже самое что и у алерта только есть 2 вариант кнопка отмена 
#    driver.switch_to.alert.accept()
#    driver.switch_to.alert.dismiss()

# алерт это prompt
#    driver.switch_to.alert.send_keys('asdsada')
#    driver.switch_to.alert.accept()
#    driver.switch_to.alert.dismiss()

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
    driver.get('https://erikdark.github.io/QA_autotests_12/')

    # ниже пишем свой код   
    driver.find_element(By.ID,'startTaskBtn').click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.send_keys('50')
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.alert.accept()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()



#Задача на поиск верной кнопки и сверка ответа и ввода
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
    driver.get('https://erikdark.github.io/Qa_autotest_01/')

    # ниже пишем свой код   
    input_text  = 'Hello World'
    driver.find_element(By.ID,'inputField').send_keys(input_text)
    buttons = driver.find_elements(By.CLASS_NAME,'btn')

    for button in buttons:
        button.click()
        time.sleep(1)
        try:
            driver.switch_to.alert.accept()
       
        except:
            pass

        output = driver.find_element(By.ID,'output').text
        if output == input_text:
            break   
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()