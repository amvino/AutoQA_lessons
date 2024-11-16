import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/Qa_autotests_05/')

    txt = driver.find_element(By.ID,'challenge').text

    nums = re.findall(r'\d+', txt)
    int[nums]
 


    #driver.find_element(By.ID,'notHuman').click()
   # driver.find_element(By.ID,'robot').click()
   # driver.find_element(By.ID,'submitBtn').click()

finally:
    time.sleep(5)
    driver.quit()
