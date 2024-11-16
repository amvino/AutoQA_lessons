import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/predki_roditeli_css/')


    # ниже пишем свой код
   
    # конец блока с моим кодом


#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
#закрываем сессию браузера
    time.sleep(3)
    driver.quit()
