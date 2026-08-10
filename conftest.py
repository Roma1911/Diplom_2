import random
import string
import pytest
import requests
import allure


BASE_URL = "https://stellarburgers.education-services.ru/api"
DEFAULT_EMAIL = "test@example.com" 
DEFAULT_PASSWORD = "testpassword123"

@allure.title("Генерируем случайную строку")
def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@allure.title("Генерируем случайны email")
def random_email():
    return f"{random_string()}@{DEFAULT_EMAIL.split('@')[1]}" 

@pytest.fixture(scope="function")
@allure.title("Создаёт нового пользователя и удаляет после теста")
def new_user():
    email = random_email()
    password = DEFAULT_PASSWORD
    name = random_string()
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": email, "password": password, "name": name}
    )
    user_data = {
        "email": email,
        "password": password,
        "name": name,
        "access_token": response.json()["accessToken"],
        "refresh_token": response.json()["refreshToken"]
    }
    yield user_data
    requests.delete(
        f"{BASE_URL}/auth/user",
        headers={"Authorization": user_data["access_token"]}
    )

@pytest.fixture(scope="function")
@allure.title("Создаёт нового пользователя и не удаляет его")
def existing_user():
    email = random_email()
    password = DEFAULT_PASSWORD
    name = random_string()
    requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": email, "password": password, "name": name}
    )
    return {"email": email, "password": password, "name": name}

@pytest.fixture(scope="function")
@allure.title("Получает ID игредиентов")
def ingredient_ids():
    response = requests.get(f"{BASE_URL}/ingredients")
    ingredients = response.json()["data"]
    return [ingredients[0]["_id"], ingredients[1]["_id"]]

@pytest.fixture(scope="function")
@allure.title("Возвращает заголовок с токеном авторизации")
def auth_header(new_user):
    return {"Authorization": new_user["access_token"]}