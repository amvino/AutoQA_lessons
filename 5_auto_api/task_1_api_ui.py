import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def get_rate_back():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    API_KEY = '33c9956b2d195185b95cb1a1'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate_back = data["rates"].get("EUR")
    return rate_back


def get_rate_front():
    try:
        driver = webdriver.Chrome()
        driver.get('https://x-rates.com/')
        driver.find_element(By.ID,'amount').send_keys('1')
        driver.find_element(By.ID,'from').send_keys('EUR - Euro')
        driver.find_element(By.ID,'to').send_keys('USD - US Dollar')
        driver.find_element(By.CSS_SELECTOR,'[href="https://www.x-rates.com/calculator/"]').click()
        
        WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.CLASS_NAME,'ccOutputRslt')))
        rate_front = driver.find_element(By.CLASS_NAME,'ccOutputRslt').text[:4]
        
    finally:
        driver.quit()
    return float(rate_front.split()[0])


def test_front_back_rate():
    rate_back = round(get_rate_back(),2)
    rate_front = round(get_rate_front(),2)

    assert rate_back == rate_front, f"Курсы не совпадают: API {rate_back}, Front {rate_front}"


#test_front_back_rate()