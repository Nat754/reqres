from requests import Response


class Assertions:
    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}. Actual: {actual_status_code}"
