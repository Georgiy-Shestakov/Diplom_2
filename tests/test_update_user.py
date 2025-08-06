import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import allure
import pytest
from data.user import generate_user_data
from methods.user_methods import UserMethods
from models.user import CreatedUser


# Тесты на изменение данных пользователя
class TestUpdateUser:

    @allure.title('Можно изменить информацию по пользователю с авторизацией')
    @pytest.mark.parametrize('update_field', ['email', 'password', 'name'])
    def test_update_user_with_authorization(self,
                                                          create_user: CreatedUser,
                                                          update_field: str) -> None:
        status_code, response_data = UserMethods.update(
            update_data={update_field: generate_user_data()[update_field]},
            access_token=create_user.access_token)
        
        assert (status_code == 200 and
                isinstance(response_data, dict) and
                response_data['success'] is True)


    @allure.title('Ошибка 401 при попытке изменения информации о пользователе без авторизации')
    @pytest.mark.parametrize('update_field', ['email', 'password', 'name'])
    def test_update_user_data_error_without_authorization(self,
                                                                       create_user: CreatedUser,
                                                                       update_field: str) -> None:
        status_code, response_data = UserMethods.update(
            update_data={update_field: generate_user_data()[update_field]})
        
        assert (status_code == 401 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == 'You should be authorised')
