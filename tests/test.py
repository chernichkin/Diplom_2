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
        print(response.json())
        response1 = requests.get(Endpoints.END_USER, headers={'Authorization': response.json()['accessToken']})
        updated_profile = {'email': 'btorres01010@gmail.com', 'name': 'Vincent Zola'}
        print(response1.json())
        print(response1.status_code)
        response2 = requests.patch(Endpoints.END_USER, headers={'Authorization': response.json()['accessToken']}, data=updated_profile)
        print(response2.json())
        print(response2.status_code)
        token = response.json()['accessToken']
        headers = {'Authorization': token}
        requests.delete(Endpoints.END_USER, headers=headers)


TestLoginUser().test_login_new_user_with_uncorrect_password_true_200()