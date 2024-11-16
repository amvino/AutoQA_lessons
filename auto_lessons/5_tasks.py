#Задание:
#По очереди нажмите на все 3 кнопки ( по очереди значит сначала напишите код для нажатия на 1 кнопку, потом закомментируйте сделайте для 2 проверьте, закомментируйте сделайте для 3). потому что если вы сделаете все 3 сразу, они не сработают так как алерты вы пока не умеете закрывать https://erikdark.github.io/predki_roditeli_css/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#инициализирую драйвер
driver = webdriver.Chrome()

# путь до страницы
driver.get('https://erikdark.github.io/predki_roditeli_css/')

# тут пишем код
# driver.find_element(By.CSS_SELECTOR,'.level-1 button').click()
# driver.find_element(By.CSS_SELECTOR,'.container .level-1 .level-2 button').click()
driver.find_element(By.CSS_SELECTOR,'.container .level-1 .level-2 .level-3 button').click()

time.sleep(3)
driver.quit()


#Задание, заполнить форму и нажать на кнопку
#Чтобы заполнить поле input - его сначала надо получить а затем применить метод send_keys(‘тут пишем текст’) https://erikdark.github.io/Qa_autotest_02/
#Решение:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    # путь до страницы
    driver.get('https://erikdark.github.io/Qa_autotest_02/')

    # ниже пишем свой код
    driver.find_element(By.ID,'phone').send_keys('7218312')
    driver.find_element(By.ID,'email').send_keys('erik@mail.ru')
    driver.find_element(By.ID,'name').send_keys('erik')
    driver.find_element(By.ID,'password').send_keys('7218312')
    driver.find_element(By.ID,'submitBtn').click()
    # конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
