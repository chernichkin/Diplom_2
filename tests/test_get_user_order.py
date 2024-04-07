import requests
import pytest
import allure
from faker import Faker
from constants import *


class TestGetUserOrder:

    @allure.title('Проверка получения заказов у авторизованного пользователя, при имеющихся двух заказах')
    def test_get_user_order_with_authorisation_two_burger_success(self, create_user_and_delete):
        user = create_user_and_delete
        headers = {'Authorization': user.json()['accessToken']}
        requests.post(Endpoints.ORDER, data=Data.ingredients_hash, headers=headers)
        requests.post(Endpoints.ORDER, data=Data.ingredients_hash, headers=headers)
        response = requests.get(Endpoints.ORDER, headers=headers)
        r = response.json()
        assert r['success'] and r['orders'][0]['ingredients'] == Data.ingredients_hash['ingredients']

    @allure.title('Проверка попытки получения заказов у неавторизованного пользователя')
    def test_get_user_order_without_authorisation_401(self, create_user_and_delete):
        user = create_user_and_delete
        headers = {'Authorization': user.json()['accessToken']}
        requests.post(Endpoints.ORDER, data=Data.ingredients_hash, headers=headers)
        response = requests.get(Endpoints.ORDER)
        r = response.json()
        assert not r['success'] and response.status_code == 401 and r['message'] == ErrorMassage.NOT_AUTHORISED
