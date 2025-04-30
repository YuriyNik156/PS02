# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры
# (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests

# Использование API
url = "https://jsonplaceholder.typicode.com/posts"

# GET-запрос с параметром userId, равный 1
params = {
    "userId" : 1
}

# Печать записи
response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(response.json())
else:
    print("Error")