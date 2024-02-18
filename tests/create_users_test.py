import allure
from base.assertions import Assertions
from data.constant import StatusCode, Constant
from base.methods import BaseRequests


@allure.epic("Create User")
class TestCreateUser:
    status = StatusCode
    constant = Constant

    @allure.title("POST Создать пользователя")
    def test_post_create_user(self):
        response = BaseRequests.post(url='', headers=self.constant.CREATE_USER)
        Assertions.assert_code_status(response, self.status.STATUS_CODE_201)
