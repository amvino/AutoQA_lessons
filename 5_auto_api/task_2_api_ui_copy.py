import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def get_backend():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
    "q": "Kaliningrad",
   "appid": "1716b91f56f380231d3e3325e096413e",  # Замените на ваш ключ OpenWeatherMap
   "units": "metric",
   "lang": "ru"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json() 
        temperature = data["main"]["temp"]
        print(temperature)
    else:
        print(f"Ошибка при запросе API: {response.status_code}")
    
    return temperature
    

get_backend()

def get_front():
    try:
        driver = webdriver.Chrome()
        driver.get('https://openweathermap.org')
        
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[placeholder = "Search city"]'))).send_keys('Kaliningrad')
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[class="button-round dark"]'))).click()   
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Kaliningrad, RU "]'))).click() 
    ???    temp = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.heading'))).text
        print(temp)
        tempr = re.findall(r'-?\d+', temp)
        print(tempr)
        temperature = int(tempr[0])
        print(temperature)


    finally:
        time.sleep(3)
        driver.quit()

get_front()


def test_front_back_rate():
    temperature_back = int(get_rate_back())
    temperature_front = int(get_rate_front())

    assert temperature_back == temperature_front, f"Температура не совпадает: API {temperature_back}, Front {temperature_front}"