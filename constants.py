import pytest


class Endpoints:
    URL = 'https://stellarburgers.nomoreparties.site/'
    END_REGISTER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    END_DELETE = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    END_LOGIN = 'https://stellarburgers.nomoreparties.site/api/auth/login'


class ErrorMassage:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
