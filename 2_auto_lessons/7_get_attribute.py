#Не всегда нам нужна информация, которая отображается на странице, иногда нам нужны данные, которые уходят на сервер, они заносятся обычно в атрибутах. Чтобы считывать атрибуты и их значения, есть метод  get_attribute

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://www.google.com/')

    # ниже пишем свой код
    a = driver.find_element(By.NAME,'btnK')
    b = a.get_attribute('data-ved')
    print(b)
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
