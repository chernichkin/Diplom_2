import requests
import pytest
from faker import Faker
from constants import *


@pytest.fixture(scope='function')
def create_user_and_delete():
    fake = Faker()
    email = fake.email()
    name = fake.name()
    password = Data.password
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(Endpoints.END_REGISTER, data=payload)
    yield response
    token = response.json()['accessToken']
    headers = {'Authorization': token}
    requests.delete(Endpoints.END_USER, headers=headers)

@pytest.fixture(scope='function')
def create_user_for_login_and_delete():
    fake = Faker()
    email = fake.email()
    name = fake.name()
    password = Data.password
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(Endpoints.END_REGISTER, data=payload)
    login_payload = {'email': email, 'password': password}
    token = response.json()['accessToken']
    yield login_payload, token
    headers = {'Authorization': token}
    requests.delete(Endpoints.END_USER, headers=headers)



