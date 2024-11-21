
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def get_backend():
    url = "https://api.aviationstack.com/v1/flights"
    params = {
    "flight_icao" : "THY404",
    "access_key" : "aa497b3288d8057087c18b0ee84e8738"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json() 
        print(data)
        flight_date = data["data"][0]["flight_date"]
        flight_status = data["data"][0]["flight_status"]
        print(flight_date)
        print(flight_status)
    else:
        print(f"Ошибка при запросе API: {response.status_code}")
    
    return flight_status, flight_date
    
get_backend()


def get_front():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.flightaware.com/')
        
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'s2id_autogen2'))).send_keys('THY404')
        
        assert WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[class="flight_ident"]'))).text == 'THY404', "данные о рейсе отсутствуют"
        
        date = driver.find_element(By.CSS_SELECTOR, '.flightPageSummaryOrigin span.flightPageSummaryDepartureDay').text

#<span class="flightPageSummaryDepartureDay">пятница 22 ноя 2024</span>

        status = 

        return date, status


    finally:
        time.sleep(3)
        driver.quit()

get_front()


def test_front_back_rate():
    
    assert date == flight_date, f"Даты не совпадает: API {flight_date}, Front {date}"
    assert status == flight_status, f"Статусы не совпадает: API {flight_status}, Front {status}"