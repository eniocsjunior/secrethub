from pytest import fixture
from faker import Faker
from secrethub import Secret

@fixture(scope='session')
def secret() -> Secret:
    return Secret(key=Secret.new)

@fixture
def message() -> str:
    return Faker().text()
