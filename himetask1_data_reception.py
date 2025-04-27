# Задание 1: Получение данных
# 1. Импортируйте библиотеку `requests`.
# 2. Отправьте GET-запрос к открытому API (например, [https://api.github.com](https://api.github.com/))
# с параметром для поиска репозиториев с кодом html.
# 3. Распечатайте статус-код ответа.
# 4. Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

# Параметры запроса
params = {
    "q" : "html"
}

# Отправка GET-запроса
response = requests.get("https://api.github.com/search/repositories", params=params)

# Печать статус-кода
print(response.status_code)

# Печать содержимого ответа в формате JSON
response_json = response.json()

pprint.pprint(response_json)

