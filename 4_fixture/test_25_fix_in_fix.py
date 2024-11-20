import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def simple_data():
    return {'name':'Erk','age':28}


def test_simple_data(simple_data):
    assert simple_data['name'] == 'Erk'
    assert simple_data['age'] == 30

#Фикстура simple_data() возвращает словарь. Тест принимает фикстуру, как аргумент, а pytest автоматически передает результат работы фикстуры в тестовую функцию.
