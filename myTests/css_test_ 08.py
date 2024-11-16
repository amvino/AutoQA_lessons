import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_autotests_09/')

    txt = driver.find_element(By.ID,'challenge').text
    nums = re.findall(r'\d+', txt)
    fst_num = int(nums[0])
    snd_num = int(nums[1])

    summa = fst_num + snd_num

    select =  Select(driver.find_element(By.CSS_SELECTOR,'.container select'))
    select.select_by_value(str(summa))

    time.sleep(1)
    driver.find_element(By.ID,'submitBtn').click()



finally:
    time.sleep(5)
    driver.quit()