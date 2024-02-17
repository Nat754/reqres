import allure

from base.assertions import Assertions
from data.constant import StatusCode
from base.methods import BaseRequests


@allure.epic("GET")
class TestAPI:

    @allure.title("GET Получить список пользователей")
    def test_get_users(self):
        response = BaseRequests.get('')
        Assertions.assert_code_status(response, StatusCode.STATUS_CODE_200)

    @allure.title("GET Получить список пользователей неверный эндпоинт")
    def test_get_users_(self):
        response = BaseRequests.get('/str')
        Assertions.assert_code_status(response, StatusCode.STATUS_CODE_404)
