# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры
# (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests
import pprint

# Использование API
url = "https://jsonplaceholder.typicode.com/posts"

# GET-запрос с параметром userId, равный 1
params = {
    "userId" : 1
}

# Печать записи
response = requests.get(url, params=params)

pprint.pprint(response.json())