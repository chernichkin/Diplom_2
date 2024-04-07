import requests
import pytest
from faker import Faker
from constants import *


class TestLoginUser:

    def test_login_new_user_with_uncorrect_password_true_200(self):
        fake = Faker()
        email = fake.email()
        name = fake.name()
        password = Data.password
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(Endpoints.END_REGISTER, data=payload)
        email1 = response.json()['user']['email']
        response_log = requests.post(Endpoints.END_LOGIN, data={'email': email1, 'password': Data.wrong_password})
        r = response_log.json()
        print(r)
        print(response_log.status_code)
        token = response.json()['accessToken']
        headers = {'Authorization': token}
        requests.delete(Endpoints.END_DELETE, headers=headers)


TestLoginUser().test_login_new_user_with_uncorrect_password_true_200()