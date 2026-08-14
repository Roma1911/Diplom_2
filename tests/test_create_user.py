import pytest
import requests
from conftest import BASE_URL
from data import MISSING_FIELDS_DATA
import allure
from constants import (
    REGISTER_USER_EXISTS_ERROR,
    MISSING_FIELDS_ERROR,
    SUCCESS_KEY,
    FOUR_HUNDRED_THREE
)

@allure.title("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self, new_user):
        assert new_user["email"] is not None
        assert new_user["access_token"] is not None
        assert new_user["refresh_token"] is not None

    @allure.title("создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, existing_user):
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=existing_user
        )
        assert response.status_code == FOUR_HUNDRED_THREE
        assert response.json()[SUCCESS_KEY] is False
        assert response.json()["message"] == REGISTER_USER_EXISTS_ERROR

    @allure.title("создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize("body", MISSING_FIELDS_DATA)
    def test_create_user_missing_field(self, body):
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=body
        )
        assert response.status_code == FOUR_HUNDRED_THREE
        assert response.json()[SUCCESS_KEY] is False
        assert response.json()["message"] == MISSING_FIELDS_ERROR