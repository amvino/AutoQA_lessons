import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/Qa_autotest_07/')

    txt = driver.find_element(By.ID,'challenge').text
    fst_num = re.findall(r'\d+', txt)
    fst_num = int(fst_num[0])
    elem = driver.find_element(By.ID,'numberImage')
    snd_num = int(elem.get_attribute('data-b'))
    summa = fst_num + snd_num
    print(summa)

    driver.find_element(By.ID,'answer').send_keys(str(summa)) 
    time.sleep(1)
    driver.find_element(By.ID,'submitBtn').click()

finally:
    time.sleep(5)
    driver.quit()