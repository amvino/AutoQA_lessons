import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #инициализирую драйвер
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/Qa_autotests_06/')

    elem = driver.find_element(By.ID,'challenge')
    fst_num = int(elem.get_attribute('data-a'))
    scnd_num = int(elem.get_attribute('data-b'))
    summa = fst_num + scnd_num
    print(summa)

    driver.find_element(By.ID,'answer').send_keys(str(summa))   

    driver.find_element(By.ID,'notRobot').click()
    driver.find_element(By.ID,'cool').click()
    time.sleep(1)
    driver.find_element(By.ID,'submitBtn').click()



finally:
    time.sleep(5)
    driver.quit()