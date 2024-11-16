import time
from selenium import webdriver
from selenium.webdriver.common.by import By #Класс By в selenium предназначен для поиска элементов на веб-странице.

#инициализирую драйвер
driver = webdriver.Chrome()

driver.get('https://erikdark.github.io/class_by_find_element_tutorial/')
time.sleep(10)

#By.id - ищет элементы по id
driver.find_element(By.ID,'btn-id').click()

#By.name - ищем по значению атрибута name
driver.find_element(By.NAME,'btn-name').click()

#By.classname - ищем элемент по значению атрибута class
driver.find_element(By.CLASS_NAME,'btn-class').click()

#By.tagname - ищет элемент по тегу. 
driver.find_element(By.TAG_NAME,'button').click()

#By.link_text  - ищет ссылки по их тексту
driver.find_element(By.LINK_TEXT,'Найти через текст ссылки').click()

#By.partial_link_text - ищем ссылку по части совпадения.
driver.find_element(By.PARTIAL_LINK_TEXT,'частичный').click()

#By.CSS_SELECTOR - ищет элементы с помощью CSS селекторов.
driver.find_element(By.CSS_SELECTOR,'[onclick="showAlert(\'Нашел через текст ссылки\')"]').click()
#В примере выше из-за одинаковых кавычек, пришлось делать экранирование , делается это так, перед кавычками которые надо экранировать ставим \’ содержимое  \’

#By.XPATH - ищет выражения по относительному пути.
driver.find_element(By.XPATH,"//div[@class='container']/button").click()

time.sleep(3)
driver.quit()
