import requests
import pytest
import allure
from faker import Faker
from constants import *


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией и ингридиентами')
    def test_create_order_with_authorization_and_ingredients_success(self, create_user_and_delete):
        user = create_user_and_delete['response']
        headers = {'Authorization': user.json()['accessToken']}
        response = requests.post(Endpoints.URL + Endpoints.ORDER, data=Data.ingredients_hash, headers=headers)
        r = response.json()
        assert r['success'] and response.status_code == 200 and r['name'] == Data.burger_name

    @allure.title('Проверка попытки создания заказа с авторизацией без ингридиентов')
    def test_create_order_with_authorization_without_ingredients_400(self, create_user_and_delete):
        user = create_user_and_delete['response']
        headers = {'Authorization': user.json()['accessToken']}
        response = requests.post(Endpoints.URL + Endpoints.ORDER, data=Data.ingredients_hash_none, headers=headers)
        r = response.json()
        assert not r['success'] and response.status_code == 400 and r['message'] == ErrorMassage.NO_INGREDIENTS

    @allure.title('Проверка создания заказа без авторизации с ингридиентами')
    def test_create_order_without_authorization_success(self, create_user_and_delete):
        response = requests.post(Endpoints.URL + Endpoints.ORDER, data=Data.ingredients_hash)
        r = response.json()
        assert r['success'] and response.status_code == 200 and r['name'] == Data.burger_name

    @allure.title('Проверка создания заказа с авторизацией с неверным хэшем ингридентов')
    def test_create_order_with_authorisation_with_bad_hash_500(self, create_user_and_delete):
        user = create_user_and_delete['response']
        headers = {'Authorization': user.json()['accessToken']}
        response = requests.post(Endpoints.URL + Endpoints.ORDER, data=Data.ingredients_bad_hash, headers=headers)
        assert response.status_code == 500
