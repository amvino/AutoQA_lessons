import pytest

@pytest.fixture(scope="module")
def module_level_setup():
    print('start')
    yield
    print('stio')


def test_one(module_level_setup):
    print('blabla')


def test_two(module_level_setup):
    print('blablabla')