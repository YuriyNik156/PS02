# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных
# (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.

import requests

# Создание словаря с данными для отправки
data = {
    "title" : "foo",
    "body" : "bar",
    "userId" : 1
}

# Использование API
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# Печать статус-кода и содержимое ответа
print(response.status_code)

print(f"ответ - {response.json()}")
