from faker import Faker


def generate_user_data() -> dict[str, str]:
    fake = Faker()
    return {'email': fake.email(),
            'password': fake.password(),
            'name': fake.name()}

class UserErrorMsgs:
    user_already_exists_error_msg = 'User already exists'
    required_fields_error_msg = 'Email, password and name are required fields'
    get_data_without_authorization_error_msg = 'You should be authorised'
    wrong_creds_error_msg = 'email or password are incorrect'