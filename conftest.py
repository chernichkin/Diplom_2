import requests
import pytest
from faker import Faker
from constants import Endpoints


@pytest.fixture(scope='function')
def create_user():
    fake = Faker()
    email = fake.email()
    name = fake.name()
    password = '111111'
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(Endpoints.END_REGISTER, data=payload)
    yield response
    token = response.json()['accessToken']
    headers = {'Authorization': token}
    requests.delete(Endpoints.END_DELETE, headers=headers)



