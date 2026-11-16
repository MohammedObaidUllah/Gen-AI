import requests

url = "https://jsonplaceholder.typicode.com/posts"

title = input("Enter title: ")
description = input("Enter description: ")

user_input = {
    "title": title,
    "body": description,
    "userId": 1
}

response = requests.post(url, json=user_input)
print("Status Code:", response.status_code)
data = response.json()
print(data["id"])
print(data["title"])