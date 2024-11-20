#Открыть страницу с таблицей данных
#Получить все колонки и данные оттуда по колонкам
#Нажать на ячейку возраст, получить и проверить что сообщение “Таблица отсортирована по столбцу 2” появилось, а также проверить, что данные которые вы считали в начале и отсортировали соответствуют тому что получилось в результате нажатия на кнопку.

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sort_table():
     browser = webdriver.Chrome()
     browser.get('https://erikdark.github.io/zachet_selenium_01/table.html')
     
     table = browser.find_element(By.ID,'data-table')
     rows = table.find_elements(By.TAG_NAME,'tr')[1:]
     orig_d = []
     for i in rows:
          cells = i.find_elements(By.TAG_NAME,'td')
          row_data = {
               'name': cells[0].text,
               'age': int(cells[1].text),
               'city': cells[2].text
          }

          orig_d.append(row_data)
          orig_d.sort(key=lambda x: x['age'],reverse=True)
          print(orig_d)
          browser.find_element(By.CSS_SELECTOR,'th[onclick="sortTable(1)"]').click()

          assert browser.find_element(By.ID,'sort-message').text == 'Таблица отсортирована по столбцу 2'

          row_after_sort = table.find_elements(By.TAG_NAME,'tr')[1:]
          sorted_table_data = []
          for i in row_after_sort:
            cells = i.find_elements(By.TAG_NAME,'td')
            row_data = {
                'name': cells[0].text,
                'age': int(cells[1].text),
                'city': cells[2].text
            }

            sorted_table_data.append(row_data)
           
     assert orig_d == sorted_table_data