from faker import Faker

faker = Faker('En')
Faker.seed()


class Constant:
    BASE_URL = 'https://reqres.in/'
    WRONG_URL = 'http://reqres.in/'


class StatusCode:
    STATUS_CODE_200 = 200
    STATUS_CODE_201 = 201
    STATUS_CODE_404 = 404


class Data:
    CREATE_USER = {"name": faker.name(), "job": faker.job()}
    NAME_USER = {"name": faker.name()}
    JOB_USER = {"job": faker.job()}
    CREATE_USER_NAME_NONE = {"name": None, "job": faker.job()}
    CREATE_USER_JOB_NONE = {"name": faker.name(), "job": None}
    LIST_KEY = ['id', 'createdAt', 'name', 'job']
