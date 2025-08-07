import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import allure
import pytest
from methods.user_methods import UserMethods
from models.user import CreatedUser
from data.user import UserErrorMsgs


# Тесты на создание пользователя
class TestCreateUser:
    
    @allure.title('Можно создать пользователя')
    def test_create_user_positive(self, create_user_with_status: tuple[int, CreatedUser]) -> None:
        status_code, created_user = create_user_with_status
        response_data = created_user.response_data
        
        assert (status_code == 200 and
                isinstance(response_data, dict) and
                response_data['success'] is True)


    @allure.title('Ошибка при создании уже существующего пользователя')
    def test_create_user_already_exists_error(self,
                                                                 create_user: CreatedUser) -> None:
        status_code, response_data = UserMethods.register(user_data=create_user.register_data)
        
        assert (status_code == 403 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == UserErrorMsgs.user_already_exists_error_msg)


    @allure.title('Ошибка при создании пользователя без required полей')
    @pytest.mark.parametrize('excluded_field', ['email', 'password', 'name'])
    def test_create_user_without_required_fields_error(self,
                                                                      user_data: dict[str, str],
                                                                      excluded_field: str) -> None:
        user_data.pop(excluded_field)
        status_code, response_data = UserMethods.register(user_data=user_data)
        
        assert (status_code == 403 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == UserErrorMsgs.required_fields_error_msg)
