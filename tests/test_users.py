import allure
import pytest


@allure.epic("Assertions")
@allure.feature("Users")
class TestUsers():

    @pytest.mark.regression
    @allure.title("Assert int")
    def test_create_user(self):
        assert 1 == 0


