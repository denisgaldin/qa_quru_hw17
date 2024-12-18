from http.client import responses

import requests

url = 'https://reqres.in/api/'


def test_single_user():
    user_id = 4
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 200


def test_negative_single_user():
    user_id = 44
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 404


def test_login_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url + f"login", json=payload)
    assert response.status_code == 200


def test_login_failed():
    payload = {
        "email": "peter@klaven"
    }
    response = requests.post(url + f"login", json=payload)
    assert response.status_code == 400


def test_create_new_users():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url + f"users", json=payload)
    assert response.status_code == 201


def test_update_users():
    payload = {
        "name": "Denis",
        "job": "AQA"
    }
    user_id = 2
    response = requests.put(url + f"users/{user_id}", json=payload)
    assert response.status_code == 200


def test_delete_users():
    user_id = 4
    response = requests.delete(url + f"users/{user_id}")
    assert response.status_code == 204
