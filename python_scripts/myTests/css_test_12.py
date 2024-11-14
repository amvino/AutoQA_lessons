import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotests_12/')

    driver.find_element(By.ID,'startTaskBtn').click()
    driver.switch_to.alert.accept()
    txt = driver.switch_to.alert.text
    nums = re.findall(r'\d+', txt)

    fst_num = int(nums[0])
    snd_num = int(nums[1])
    summa = fst_num + fst_num
    
    driver.switch_to.alert.send_keys(str(summa))
    time.sleep(1)
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()


finally:
    time.sleep(5)
    driver.quit()