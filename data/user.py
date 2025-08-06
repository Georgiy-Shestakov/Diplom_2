from faker import Faker


def generate_user_data() -> dict[str, str]:
    fake = Faker()
    return {'email': fake.email(),
            'password': fake.password(),
            'name': fake.name()}
