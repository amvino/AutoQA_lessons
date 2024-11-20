#Если бы мы писали автотест на эти вещи:
import requests
import pytest

API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '1716b91f56f380231d3e3325e096413e'

@pytest.fixture
def api_params():
    return {
        "q": "Kaliningrad",
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

def test_status_code(api_params):
    response = requests.get(API_URL,params=api_params)
    assert response.status_code == 200


def test_temperature(api_params):
    response = requests.get(API_URL,params=api_params)
    data = response.json()
    assert "main" in data
    assert "temp" in data["main"]


def test_weather_description_field(api_params):
    response = requests.get(API_URL,params=api_params)
    data = response.json()
    assert "weather" in data
    assert len(data["weather"]) >0
    assert "description" in data["weather"][0]