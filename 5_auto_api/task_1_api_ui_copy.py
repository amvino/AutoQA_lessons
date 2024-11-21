import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


def get_exchange_rate_from_api():
    api_url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data["rates"].get("EUR")
    else:
        print('Ошибка в запросе.')


def get_exchange_rate_from_site():
    driver  = webdriver.Chrome()
    driver.get('https://www.x-rates.com/table/?from=USD&amount=1')

    try:
        rows = driver.find_elements(By.CSS_SELECTOR,'tr')
        euro_rate = None

        for i in rows:
            if "Euro" in i.text:
                cells = i.find_elements(By.CSS_SELECTOR,'td')
                if len(cells) > 1:
                    euro_rate = float(cells[1].text)
                break
        if euro_rate is None:
            print('Курс евро не найден')
    finally:
        driver.quit()

    return euro_rate


def test_change_rate():
    api_rate = get_exchange_rate_from_api()
    print(f'Курс из API: {round(api_rate,2)}' )
    api_rate = round(api_rate,2)
    site_rate = get_exchange_rate_from_site()
    print(f'Курс с сайта: {round(site_rate,2)}')
    site_rate = round(site_rate,2)

    assert api_rate == site_rate, 'данные не совпадают'

test_change_rate()
