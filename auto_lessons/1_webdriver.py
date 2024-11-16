
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://easysmarthub.ru')
time.sleep(5)

driver.quit()
