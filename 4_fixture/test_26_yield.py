import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def resorce_setup():
    #настройка ресурса
    print('Команды перед запуском')
    resurce = {'connection':'connected'}
    yield
    #Очистка ресурса
    print('Подчищаем за собой после теста')
    resurce['connection'] = 'disconnected'


def test_using_resurce(resorce_setup):
    assert resorce_setup['connection'] == 'connected'

#Код до yield выполняется до теста(настройка)  Код после yield выполняется после теста(очистка)