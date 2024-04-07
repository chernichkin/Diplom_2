import requests
import pytest
from faker import Faker
from constants import *


class TestLoginUser:

    def test_change_user_data_all_success(self, create_user_and_delete):
        user = create_user_and_delete
        response = requests.patch(Endpoints.END_USER,
                                  headers={'Authorization': user.json()['accessToken']},
                                  data=Data.updated_profile)
        r = response.json()
        assert r["success"] and r['user']['email'] == Data.updated_profile['email'] and r['user']['name'] == \
               Data.updated_profile[
                   "name"]

    def test_change_user_data_without_autorithation_false(self, create_user_and_delete):
        # создаем новго юзера
        user = create_user_and_delete
        response = requests.patch(Endpoints.END_USER,
                                  data=Data.updated_profile)
        r = response.json()
        assert not r["success"] and response.status_code == 401 and r["message"] == ErrorMassage.NOT_AUTHORISED
