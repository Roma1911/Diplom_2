import random
import string
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
