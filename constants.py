import pytest


class Endpoints:
    URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER = '/api/auth/register'
    USER = '/api/auth/user'
    LOGIN = '/api/auth/login'
    ORDER = '/api/orders'


class ErrorMassage:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    WRONG_EMAIL_OR_PASSWORD = "email or password are incorrect"
    NOT_AUTHORISED = "You should be authorised"
    NO_INGREDIENTS = "Ingredient ids must be provided"


class Data:
    password = '111111'
    wrong_password = '123456'
    updated_profile = {'email': 'btorres01010@gmail.com', 'name': 'Vincent Zola'}
    updated_profile_email = {'email': 'btorres01010@gmail.com', 'name': 'Vincent Zola'}
    updated_profile_name = {'name': 'Vincent Zola'}
    ingredients_hash = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6d"]
    }
    ingredients_hash_none = {
        "ingredients": []
    }
    ingredients_bad_hash = {
        "ingredients": ["111", "1234"]
    }
    burger_name = 'Люминесцентный традиционный-галактический флюоресцентный бургер'

