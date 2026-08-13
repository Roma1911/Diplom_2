Создание пользователя:
создать уникального пользователя;
создать пользователя, который уже зарегистрирован;
создать пользователя и не заполнить одно из обязательных полей.
Логин пользователя:
вход под существующим пользователем;
вход с неверным логином и паролем.
Создание заказа:
с авторизацией;
без авторизации;
с ингредиентами;
без ингредиентов;
с неверным хешем ингредиентов.

"Запустить тесты с отчётом Allure"

pytest tests/test_create_user.py --alluredir=./allure-results
allure serve ./allure-results

pytest tests/test_creating_order.py --alluredir=./allure-results
allure serve ./allure-results

pytest tests/test_login.py --alluredir=./allure-results
allure serve ./allure-results

"Запустить конкретный тест"

pytest tests/test_create_user.py -v

pytest tests/test_creating_order.py -v

pytest tests/test_login.py -v


