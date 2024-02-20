import allure
from requests import Response


class Assertions:

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        """Check status code is expected"""
        actual_status_code = response.status_code
        with allure.step(f'Expected status {expected_status_code}'):
            assert actual_status_code == expected_status_code, \
                f'Unexpected status code. Expected: {expected_status_code}. Actual: {actual_status_code}'

    @staticmethod
    def assert_response_is_json(response: Response):
        """Check response has json format"""
        with allure.step('Response is in JSON format'):
            assert 'application/json' in response.headers.get('Content-Type', ''), \
                'Error: Response is not in JSON format'

    @staticmethod
    def assert_is_not_code_status(response: Response, expected_status_code):
        """Check status code is wrong"""
        actual_status_code = response.status_code
        with allure.step(f'Expected status is not equal {expected_status_code}'):
            assert actual_status_code != expected_status_code, \
                f'Unexpected status code. Expected not {expected_status_code}. Actual: {actual_status_code}'

    @staticmethod
    def assert_key_name_is_in_response(response: Response, key_name):
        """Check if the required key is in the response"""
        json_value = response.json()
        actual_key = json_value.get(key_name)
        with allure.step(f'The key {actual_key} exist'):
            assert actual_key is not None, f'The key {actual_key} does not exist'

    @staticmethod
    def assert_key_value_is_in_response(response: Response, data, key_name):
        """Check if the required value is in the response"""
        json_value = response.json()
        actual_key = json_value[key_name]
        expected_key = data[key_name]
        with allure.step(f'Actual key is {expected_key}'):
            assert actual_key == expected_key, f'Actual key {expected_key} is not in response'

    @staticmethod
    def assert_response_is_not_empty(response: Response):
        """Check response has json format and is not empty"""
        with allure.step('Response has JSON format and is not empty'):
            assert 'application/json' in response.headers.get('Content-Type', '') and 'application/json' != {}, \
                'Error: Response is not in JSON format'
