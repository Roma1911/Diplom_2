import pytest
import requests
from conftest import BASE_URL
from data import INVALID_INGREDIENT_HASH
import allure
from constants import (
    TWO_HUNDRED,
    FOUR_HUNDRED,
    FIVE_HUNDRED,
    INGREDIENT_IDS
)


@allure.title("Создание заказа")
class TestCreatingOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, auth_header, ingredient_ids):
        response = requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": ingredient_ids},
            headers=auth_header
        )
        assert response.status_code == TWO_HUNDRED
        assert response.json()["success"] is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self, ingredient_ids):
        response = requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": ingredient_ids}
        )
        assert response.status_code == TWO_HUNDRED
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, ingredient_ids):
        response = requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": ingredient_ids}
        )
        assert response.status_code == TWO_HUNDRED
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": []}
        )
        assert response.status_code == FOUR_HUNDRED
        assert response.json()["success"] is False
        assert response.json()["message"] == INGREDIENT_IDS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self):
        response = requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": [INVALID_INGREDIENT_HASH]}
        )
        assert response.status_code == FIVE_HUNDRED
