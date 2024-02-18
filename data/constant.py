from faker import Faker

faker = Faker('En')
Faker.seed()


class Constant:
    BASE_URL = 'https://reqres.in/api/users'

    CREATE_USER = {"name": faker.name(), "job": faker.job()}


class StatusCode:
    STATUS_CODE_200 = 200
    STATUS_CODE_201 = 201
    STATUS_CODE_404 = 404
