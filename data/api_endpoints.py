SERVICE_BASE_URL = 'https://stellarburgers.nomoreparties.site'
SERVICE_API_URL = f'{SERVICE_BASE_URL}/api'


class Endpoints:
    login = f'{SERVICE_API_URL}/auth/login'
    logout = f'{SERVICE_API_URL}/auth/logout'
    orders = f'{SERVICE_API_URL}/orders'
    register = f'{SERVICE_API_URL}/auth/register'
    user = f'{SERVICE_API_URL}/auth/user'
