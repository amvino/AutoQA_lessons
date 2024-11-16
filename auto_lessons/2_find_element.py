
#Поиск элементов  с помощью CSS селекторов.
# По id: #name_id
# tag name: button
# значению атрибута: [id=”#name_id”]
# name: name = “name”
# class: .name_class

import time
from selenium import webdriver
from selenium.webdriver.common.by import By #Класс By в selenium предназначен для поиска элементов на веб-странице.

driver = webdriver.Chrome()

driver.get('https://easysmarthub.ru')
time.sleep(10)

driver.find_element(By.CSS_SELECTOR,'[href="https://easysmarthub.ru/courses/"]').click()
time.sleep(3)

driver.quit()


