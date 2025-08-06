from typing import Generator

import pytest
from data.user import generate_user_data
from methods.user_methods import UserMethods
from models.user import CreatedUser


@pytest.fixture()
def user_data() -> dict[str, str]:
    return generate_user_data()


@pytest.fixture()
def create_user(user_data: dict[str, str]) -> Generator[CreatedUser, None, None]:
    response_data = UserMethods.register(user_data=user_data)[1]
    created_user = CreatedUser(register_data=user_data,
                               response_data=response_data)
    
    yield created_user
    UserMethods.delete(access_token=created_user.access_token)
