import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "тестовый post запрос",
    "body" : "тестовый контент post запроса",
    "user id" : 2
}

response = requests.post(url, data=data)

print(response.status_code)

print(f"ответ - {response.json()}")