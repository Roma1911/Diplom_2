import pytest
import requests
from conftest import BASE_URL
from data import INVALID_LOGIN_DATA
import allure

@allure.title("Логин пользователя")
class TestLogin:

    @allure.title("вход под существующим пользователем")
    def test_login_existing_user(self, new_user):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": new_user["email"], "password": new_user["password"]}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == new_user["email"]

    @allure.title("вход с неверным логином и паролем")
    @pytest.mark.parametrize("credentials", INVALID_LOGIN_DATA)
    def test_login_invalid_credentials(self, credentials):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json=credentials
        )
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"