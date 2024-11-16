import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

val = '550'

try:
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotest_16/')

    WebDriverWait(driver,15).until(EC.text_to_be_present_in_element((By.ID,'price1'), val))
    driver.find_element(By.ID,'buyButton1').click()

    if WebDriverWait(driver,15).until(EC.text_to_be_present_in_element((By.ID,'message1'), 'Вы успешно купили автомобиль!')):
        print(f'Yep!')
    else:
        print(f'Nope!')


finally:
    time.sleep(3)
    driver.quit()
