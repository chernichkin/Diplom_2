import requests
import pytest
from faker import Faker
from constants import *


class TestLoginUser:

    def test_login_new_user_with_correct_data_true_200(self, create_user_for_login_and_delete):
        login_payload, token = create_user_for_login_and_delete
        response = requests.post(Endpoints.END_LOGIN, data=login_payload)
        r = response.json()
        assert response.status_code == 200 and r['success'] and 'Bearer' in r['accessToken']

    def test_login_new_user_with_uncorrect_password_false_401(self, create_user_and_delete):
        response = create_user_and_delete
        email = response.json()['user']['email']
        response_log = requests.post(Endpoints.END_LOGIN, data={'email': email, 'password': Data.wrong_password})
        r = response_log.json()
        assert response_log.status_code == 401 and not r['success'] and r['message'] == ErrorMassage.WRONG_EMAIL_OR_PASSWORD

    def test_login_new_user_with_uncorrect_email_false_401(self, create_user_and_delete):
        response = create_user_and_delete
        email = f'adsad{response.json()['user']['email']}'
        response_log = requests.post(Endpoints.END_LOGIN, data={'email': email, 'password': Data.password})
        assert response_log.status_code == 401
