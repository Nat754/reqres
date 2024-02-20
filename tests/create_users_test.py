import allure
import pytest
import requests

from base.assertions import Assertions
from data.constant import StatusCode, Data, Constant
from base.methods import BaseRequests


@allure.epic('Create User')
class TestCreateUser:
    status = StatusCode
    data = Data
    constant = Constant

    @allure.title('POST Create user')
    def test_post_create_user(self):
        response = BaseRequests.post(url='api/users', headers=self.data.CREATE_USER)
        Assertions.assert_code_status(response, self.status.STATUS_CODE_201)

    @allure.title('Check format is json')
    def test_post_create_user_response_is_json(self):
        response = BaseRequests.post(url='api/users', headers=self.data.CREATE_USER)
        Assertions.assert_response_is_json(response)

    @pytest.mark.parametrize('key_name', data.LIST_KEY)
    def test_post_create_user_key_name_is_in_response(self, key_name):
        allure.dynamic.title(f'Check response has key {key_name}')
        headers = self.data.CREATE_USER
        response = BaseRequests.post(url='api/users', headers=headers)
        Assertions.assert_key_name_is_in_response(response, key_name)

    @pytest.mark.xfail(reason='Bag')
    @pytest.mark.parametrize('key_value', data.CREATE_USER)
    def test_post_create_user_key_value_is_in_response(self, key_value):
        allure.dynamic.title(f'Check response has key value {key_value}')
        headers = self.data.CREATE_USER
        response = BaseRequests.post(url='api/users', headers=headers)
        Assertions.assert_key_value_is_in_response(response, headers, key_value)

    @allure.title('GET Send request get with body')
    def test_get_create_user(self):
        response = BaseRequests.get(url='api/users', headers=self.data.CREATE_USER)
        Assertions.assert_code_status(response, self.status.STATUS_CODE_200)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user without request body')
    def test_post_create_user_without_body(self):
        response = BaseRequests.post(url='api/users')
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user without job')
    def test_post_create_user_without_job(self):
        response = BaseRequests.post(url='api/users', data=self.data.NAME_USER)
        print('cod', response.status_code)
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user without name')
    def test_post_create_user_without_name(self):
        response = BaseRequests.post(url='api/users', headers=self.data.JOB_USER)
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user with None job')
    def test_post_create_user_with_none_job(self):
        response = BaseRequests.post(url='api/users', headers=self.data.CREATE_USER_JOB_NONE)
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user with None name')
    def test_post_create_user_with_none_name(self):
        response = BaseRequests.post(url='api/users', headers=self.data.CREATE_USER)
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title('POST Create user as {}')
    def test_post_create_user_as_none(self):
        response = BaseRequests.post(url='api/users', headers={})
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_201)

    @pytest.mark.xfail(reason='Bag')
    @allure.title("POST Create user get to http")
    def test_create_users_to_http(self):
        response = requests.post(url=f'{self.constant.WRONG_URL}api/users', headers=self.data.CREATE_USER)
        Assertions.assert_is_not_code_status(response, self.status.STATUS_CODE_200)

    @allure.title('POST Create user response is not empty')
    def test_post_create_user_response_is_not_empty(self):
        response = BaseRequests.post(url='api/users', headers=self.data.CREATE_USER)
        Assertions.assert_response_is_not_empty(response)
