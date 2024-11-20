# requests.get(url,params=None,kwargs)
# requests.post(url,data=None,json=None,kwargs)
import requests
import pytest


BASE_URL = 'https://jsonplaceholder.typicode.com/'


def test_posts():
    response = requests.get(f'{BASE_URL}/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data
    assert 'body' in data


def test_create_posts():
    payload = {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    }

    response = requests.post(f'{BASE_URL}/posts',json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data['title'] == payload['title']


def test_get_nonexist_posts():
    response = requests.get(f'{BASE_URL}/posts/9999')
    assert response.status_code == 404


