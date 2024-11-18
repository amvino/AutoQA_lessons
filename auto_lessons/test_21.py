#Написать автотест на покупку всех 3 машин.
#1 - Выгрышная цена 550
#2 - Выгрышная цена 800
#3 - Выйгрышная 19000

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_car_auction():
            
            driver = webdriver.Chrome()
            driver.get('https://erikdark.github.io/Qa_autotests_17/')
            try:
                #test 1
                test_car(driver,1,550)
                #test 2
                test_car(driver,2,800)
                #test 3           
                test_car(driver,3,19000)
            finally:
                driver.quit()
   
def test_car(driver,car_index,winning_price):
       
       WebDriverWait(driver,60).until(EC.text_to_be_present_in_element((By.ID,f'price{car_index}'),str(winning_price)))

       driver.find_element(By.ID,f'buyButton{car_index}').click()

       WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,f'message{car_index}')))

       assert driver.find_element(By.ID,f'message{car_index}').text == 'Вы успешно купили автомобиль!'
