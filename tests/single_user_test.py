import allure
from base.assertions import Assertions
from data.constant import StatusCode
from base.methods import BaseRequests


@allure.epic("GET Single User")
class TestAPISingleUser:
    status = StatusCode

    @allure.title("GET Получить одного пользователя с id 2")
    def test_get_single_user(self):
        response = BaseRequests.get(url='2')
        Assertions.assert_code_status(response, self.status.STATUS_CODE_200)

    @allure.title("GET Попытка получить несуществующего пользователя с id 23")
    def test_get_single_user(self):
        response = BaseRequests.get(url='/23')
        Assertions.assert_code_status(response, self.status.STATUS_CODE_404)
