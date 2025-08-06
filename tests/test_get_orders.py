import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


import allure
from data.ingredients import get_random_ingredients
from methods.order_methods import OrderMethods
from models.user import CreatedUser


# Тесты на получение заказа конкретного пользователя
class TestGetOrders:

    @allure.title('Авторизованный пользователь может получить информацию по заказам')
    def test_get_orders_with_authorization(self,
                                                    create_user: CreatedUser) -> None:
        _, create_response_data = OrderMethods.create_order(ingredients=get_random_ingredients(),
                                                            access_token=create_user.access_token)
        status_code, response_data = OrderMethods.get_orders(access_token=create_user.access_token)
        
        assert (status_code == 200 and
                (isinstance(response_data, dict) and isinstance(create_response_data, dict)) and
                response_data['success'] is True and
                create_response_data['order']['number'] == response_data['orders'][0]['number'])


    @allure.title('Неавторизованный пользователь не может получить информацию по заказам')
    def test_get_orders_without_authorization(self) -> None:
        status_code, response_data = OrderMethods.get_orders()
        
        assert (status_code == 401 and
                isinstance(response_data, dict) and
                response_data['success'] is False and
                response_data['message'] == 'You should be authorised')
