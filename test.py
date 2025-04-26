import requests

img = "https://sun9-79.userapi.com/impg/mlM8vQjOhVkVD0q80_Cr3QUCLph1sZ8_zKVKvw/QMOhABRgRNE.jpg?size=1280x723&quality=95&sign=2f7d1ad1ef56c7ca6823922457316e76&type=album"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)