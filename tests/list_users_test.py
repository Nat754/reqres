import allure
from base.assertions import Assertions
from data.constant import StatusCode
from base.methods import BaseRequests


@allure.epic("List Users")
class TestListUsers:
    status = StatusCode

    @allure.title("GET Получить список пользователей")
    def test_get_list_users(self):
        response = BaseRequests.get(url='?page=2')
        Assertions.assert_code_status(response, self.status.STATUS_CODE_200)

    @allure.title("GET Получить список пользователей неверный эндпоинт")
    def test_get_users(self):
        response = BaseRequests.get(url='/str')
        Assertions.assert_code_status(response, self.status.STATUS_CODE_404)
