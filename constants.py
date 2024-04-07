import pytest


class Endpoints:
    URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    LOGIN = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'


class ErrorMassage:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    WRONG_EMAIL_OR_PASSWORD = "email or password are incorrect"
    NOT_AUTHORISED = "You should be authorised"
    NO_INGREDIENTS = "Ingredient ids must be provided"
    BAD_INGREDIENTS = "Ingredient ids must be provided"


class Data:
    password = '111111'
    wrong_password = '123456'
    updated_profile = {'email': 'btorres01010@gmail.com', 'name': 'Vincent Zola'}
    ingredients_hash = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6d"]
    }
    ingredients_hash_none = {
        "ingredients": []
    }
    ingredients_bad_hash = {
        "ingredients": ["61c0c5a71d1f82001b111111", "61c0c5a71d1f82001b111111", "61c0c5a71d1f82001b111111", "61c0c5a71d1f82001bd111111"]
    }
    burger_name = 'Люминесцентный традиционный-галактический флюоресцентный бургер'

