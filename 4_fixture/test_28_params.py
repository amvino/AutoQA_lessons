import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(params=['chrome','firefox','safari'])
def browser(request):
    return request.param


def test_browser(browser):
    print(f'testing{browser}')
    assert browser in ['chrome','firefox','safari']
