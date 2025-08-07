import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import allure
import pytest
from methods.user_methods import UserMethods
from models.user import CreatedUser
from data.user import UserErrorMsgs


# Тесты на авторизацию (логин пользователя)
class TestLoginUser:

    @allure.title('Пользователь может успешно авторизоваться')
    def test_login_user_positive(self, create_user: CreatedUser) -> None:
        status_code, response_data = UserMethods.login(user_data=create_user.login_data)
        
        assert (status_code == 200 and
                isinstance(response_data, dict) and
                response_data['success'] is True)


    @allure.title('Ошибка при некорректных данных пользователя')
    @pytest.mark.parametrize('incorrect_field', ['email', 'password'])
    def test_login_user_with_wrong_creds_error(
            self, create_user: CreatedUser, incorrect_field: str) -> None:
        status_code, response_data = UserMethods.login(user_data={**create_user.login_data,
                                                                  incorrect_field: 'incorrect'})
        
        assert (status_code == 401 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == UserErrorMsgs.wrong_creds_error_msg)
