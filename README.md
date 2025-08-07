# Дипломный проект. Задание 2: API-тесты

### Описание
В этой части проекта разработаны API-тесты.

### Структура проекта
```

```
Diplom_2/
├── .gitignore
├── conftest.py
├── data/
│   ├── __init__.py
│   ├── api_endpoints.py
│   ├── ingredients.py
│   ├── user.py
│   └── utils.py
├── methods/
│   ├── __init__.py
│   ├── order_methods.py
│   └── user_methods.py
├── models/
│   ├── __init__.py
│   └── user.py
├── tests/
│   ├── __init__.py
│   ├── requirements.txt
│   ├── test_create_order.py
│   ├── test_create_user.py
│   ├── test_get_orders.py
│   ├── test_login_user.py
│   └── test_update_user.py
```

#### Data
- **api_endpoints.py**: Api эндпоинты.
- **ingredients.py**: Данные по ингридиентам и их получение.
- **user.py**: Генерация данных по пользователю.
- **utils.py**: Функции для использования в проекте.

#### Methods
- **order_methods.py**: Методы создания/получения заказов.
- **user_methods.py**: Пользовательские методы.

#### Tests
- **test_create_order.py**: Тесты на создание заказа.
- **test_create_user.py**: Тесты на создание пользователя.
- **test_get_orders.py**: Тесты на получение заказа конкретного пользователя.
- **test_login_user.py**: Тесты на авторизацию (логин пользователя).
- **test_update_user.py**: Тесты на изменение данных пользователя.

### Requirements
Зависимости
```bash
pip install -r tests/requirements.txt
```

### Запуск тестов
Чтобы запустить тесты, используйте ```pytest```
