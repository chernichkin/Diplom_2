import requests
import pytest
from faker import Faker
from constants import *


class TestCreateNewUser:

    def test_create_new_user_with_correct_data_true_200(self, create_user_and_delete):
        response = create_user_and_delete
        r = response.json()
        assert response.status_code == 200 and r['success'] and 'Bearer' in r['accessToken']

    def test_create_new_user_with_existing_data_error_403(self, create_user_and_delete):
        response = create_user_and_delete
        email = response.json()['user']['email']
        name = response.json()['user']['name']
        password = Data.password
        response = requests.post(Endpoints.END_REGISTER, data={'email': email, 'password': password, 'name': name})
        r = response.json()
        print(response.json())
        assert response.status_code == 403 and not r['success'] and r['message'] == ErrorMassage.USER_EXISTS

    def test_create_new_user_without_email_data_error_403(self):
        fake = Faker()
        payload = {'email': '', 'password': Data.password, 'name': fake.name}
        response = requests.post(Endpoints.END_REGISTER, data=payload)
        r = response.json()
        assert response.status_code == 403 and not r['success'] and r['message'] == ErrorMassage.REQUIRED_FIELDS
