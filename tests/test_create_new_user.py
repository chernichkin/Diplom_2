import requests
import pytest
import allure
from faker import Faker
from constants import *


class TestCreateNewUser:

    @allure.title('Проверка создания пользователя с верными тестовыми данными')
    def test_create_new_user_with_correct_data_true_200(self, create_user_and_delete):
        response = create_user_and_delete['response']
        r = response.json()
        assert response.status_code == 200 and r['success'] and 'Bearer' in r['accessToken']

    @allure.title('Проверка создания уже зарегестрированного пользователя')
    def test_create_new_user_with_existing_data_error_403(self, create_user_and_delete):
        response = create_user_and_delete['response']
        email = response.json()['user']['email']
        name = response.json()['user']['name']
        password = Data.password
        response = requests.post(Endpoints.URL + Endpoints.REGISTER, data={'email': email, 'password': password, 'name': name})
        r = response.json()
        assert response.status_code == 403 and not r['success'] and r['message'] == ErrorMassage.USER_EXISTS

    @allure.title('Проверка создания пользователя без заполнения поля почты')
    def test_create_new_user_without_email_data_error_403(self):
        fake = Faker()
        payload = {'email': '', 'password': Data.password, 'name': fake.name}
        response = requests.post(Endpoints.URL + Endpoints.REGISTER, data=payload)
        r = response.json()
        assert response.status_code == 403 and not r['success'] and r['message'] == ErrorMassage.REQUIRED_FIELDS

    @allure.title('Проверка создания пользователя без заполнения поля пароля')
    def test_create_new_user_without_password_data_error_403(self):
        fake = Faker()
        payload = {'email': fake.email, 'password': '', 'name': fake.name}
        response = requests.post(Endpoints.URL + Endpoints.REGISTER, data=payload)
        r = response.json()
        assert response.status_code == 403 and not r['success'] and r['message'] == ErrorMassage.REQUIRED_FIELDS
