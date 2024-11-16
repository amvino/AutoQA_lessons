#Замена time.sleep
#Ожидание - неявное (implicit wait) так как его не надо явно указывать, каждый раз когда мы выполняем поиск элементов. он автоматически будет применяться каждый раз при вызове последующей команды.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    #говорим WebDriver каждый элемент искать 5 секунд.
    driver.implicitly_wait(5)
    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_14/')

    # ниже пишем свой код
    driver.find_element(By.ID,'verify').click()   
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()

#Но, неявное ожидание, оно конечно заменяет time.sleep() тем не менее, может тоже быть не всегда рабочим методом или ломать масштаб теста.

#По этому придумали явные ожидание (Explicit Wait) которые позволяют задать специальное ожидание для конкретного элемента.
#Делается с помощью инструментов WebDriverWait и expected_conditions.