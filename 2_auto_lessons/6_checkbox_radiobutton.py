#Для решения задачи, нам надо получить число 1 и число 2, посчитать их сумму, записать эту сумму в поле и отменить нужные чеки и нажать на кнопку.
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
    driver.get('https://erikdark.github.io/Qa_autotests_05/')

    # ниже пишем свой код
    #Чтобы получить текст, мы используем метод .text
    challage_text = driver.find_element(By.ID,'challenge').text
    print(challage_text)

    # parts = re.findall(r'\d+',challage_text)
    parts = challage_text.split()
    print(parts)
    
    a = int(parts[2])
    b = int(parts[4].replace('?',''))
    # a = int(parts[0])
    # b = int(parts[1])

    correct_answer = a+b
    
    driver.find_element(By.ID,'answer').send_keys(str(correct_answer))
    driver.find_element(By.ID,'notRobot').click()
    driver.find_element(By.ID,'cool').click()
    time.sleep(1)
    driver.find_element(By.ID,'submitBtn').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
