import requests
import pytest
from faker import Faker
from constants import *
from helper import generate_payloads


@pytest.fixture(scope='function')
def create_user_and_delete():
    payload, login_payload = generate_payloads()
    response = requests.post(Endpoints.URL + Endpoints.REGISTER, data=payload)
    token = response.json()['accessToken']
    yield {'login_payload': login_payload, 'token': token, 'response': response}
    headers = {'Authorization': token}
    requests.delete(Endpoints.URL + Endpoints.USER, headers=headers)
