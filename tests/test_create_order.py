import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import allure
from data.ingredients import get_random_ingredients
from methods.order_methods import OrderMethods
from models.user import CreatedUser


# Тесты на создание заказа
class TestCreateOrder:
    
    @allure.title('Можно успешно создать заказ с предварительной авторизацией и ингридиентами')
    def test_create_order_with_authorization(
            self, create_user: CreatedUser) -> None:
        status_code, response_data = OrderMethods.create_order(
            ingredients=get_random_ingredients(), access_token=create_user.access_token)
        
        assert (status_code == 200 and
                isinstance(response_data, dict) and
                response_data['success'] is True and
                response_data['order'].get('owner') is not None and
                response_data['order']['owner']['name'] == create_user.register_data['name'])


    @allure.title('Можно успешно создать заказ без предварительной авторизациии')
    def test_create_order_without_authorization(self) -> None:
        status_code, response_data = OrderMethods.create_order(ingredients=get_random_ingredients())
        
        assert (status_code == 200 and
                isinstance(response_data, dict) and
                response_data['success'] is True and
                response_data['order'].get('owner') is None)


    @allure.title('Ошибка при попытке создать заказ без ингридиентов')
    def test_create_order_without_ingredients(self) -> None:
        status_code, response_data = OrderMethods.create_order()
        
        assert (status_code == 400 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == 'Ingredient ids must be provided')


    @allure.title('Ошибка при заказе с несуществующим ингридиентом')
    def test_create_order_with_unexpected_ingredient(self) -> None:
        unknown_ingredient = get_random_ingredients(1)[0][::-1]
        status_code, response_data = OrderMethods.create_order(ingredients=[unknown_ingredient])
        
        assert (status_code == 400 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == 'One or more ids provided are incorrect')


    @allure.title('Ошибка 500 при заказе с указанием невалидного хэша ингредиента')
    def test_create_order_with_invalid_hash(self) -> None:
        invalid_ingredient = get_random_ingredients(1)[0] + '1'
        status_code, _ = OrderMethods.create_order(ingredients=[invalid_ingredient])
        
        assert status_code == 500
