import json

import requests
from jsonschema import validate

url = 'https://reqres.in/api/'


def test_schema_get_user():
    user_id = 4
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 200
    with open('schemas/get_user.json') as file:
        schema = json.load(file)
    validate(instance=response.json(), schema=schema)


def test_schema_post_login():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url + f"login", json=payload)
    assert response.status_code == 200
    with open('schemas/post_login.json') as file:
        schema = json.load(file)
    validate(response.json(), schema=schema)


def test_create_new_users():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url + f"users", json=payload)
    assert response.status_code == 201
    with open('schemas/post_users.json') as file:
        schema = json.load(file)
    validate(response.json(), schema=schema)

def test_put_users():
    payload = {
        "name": "denis",
        "job": "QA"
    }
    user_id = 2
    response = requests.put(url + f"users/{user_id}", json=payload)
    assert response.status_code == 200
    with open('schemas/put_users.json') as file:
        schema = json.load(file)
    validate(instance=response.json(), schema=schema)
