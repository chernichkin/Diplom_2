import requests
import allure
import pytest
from faker import Faker
from constants import *


class TestChangeUserData:

    @allure.title('Проверка успешности патча при одновременном изменении имени и почты у авторизованного пользователя')
    def test_change_user_data_all_success(self, create_user_and_delete):
        user = create_user_and_delete
        response = requests.patch(Endpoints.URL + Endpoints.USER,
                                  headers={'Authorization': user['response'].json()['accessToken']},
                                  data=Data.updated_profile)
        r = response.json()
        assert r["success"] and response.status_code == 200

    @allure.title('Проверка изменения почты у авторизованного пользователя')
    def test_change_user_email_success(self, create_user_and_delete):
        user = create_user_and_delete
        response = requests.patch(Endpoints.URL + Endpoints.USER,
                                  headers={'Authorization': user['response'].json()['accessToken']},
                                  data=Data.updated_profile_email)
        r = response.json()
        assert r['user']['email'] == Data.updated_profile_email['email'] and response.status_code == 200

    @allure.title('Проверка изменения имени у авторизованного пользователя')
    def test_change_user_name_success(self, create_user_and_delete):
        user = create_user_and_delete
        response = requests.patch(Endpoints.URL + Endpoints.USER,
                                  headers={'Authorization': user['response'].json()['accessToken']},
                                  data=Data.updated_profile_email)
        r = response.json()
        assert r['user']['name'] == Data.updated_profile_name['name'] and response.status_code == 200

    @allure.title('Проверка попытки изменения имени и почты у неавторизованного пользователя')
    def test_change_user_data_without_authorisation_false(self, create_user_and_delete):
        response = requests.patch(Endpoints.URL + Endpoints.USER,
                                  data=Data.updated_profile)
        r = response.json()
        assert not r["success"] and response.status_code == 401 and r["message"] == ErrorMassage.NOT_AUTHORISED
