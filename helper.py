from faker import Faker
from constants import Data


def generate_payloads():
    fake = Faker()
    email = fake.email()
    name = fake.name()
    password = Data.password
    payload = {'email': email, 'password': password, 'name': name}
    login_payload = {'email': email, 'password': password}
    return payload, login_payload
