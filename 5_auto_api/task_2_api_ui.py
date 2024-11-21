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
    "appid": "1716b91f56f380231d3e3325e096413e"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json() 
        temperature = data["main"]["temp"]
        
    else:
        print(f"Ошибка при запросе API: {response.status_code}")
    
    return temperature

get_backend()