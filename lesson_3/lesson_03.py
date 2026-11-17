import requests

url = "https://jsonplaceholder.typicode.com/posts"

title = input("Enter the title: ")
description = input("Enter the description: ")

data = {
    "title": title,
    "body": description
}

try:
    response = requests.post(url, json = data)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    # print("Content-Type:", response.headers["Content-Type"])
    print("Content-Type:", response.headers.get("Content-Type"))

    python_data = response.json()

    print("POST Id:", python_data["id"])
    print("Title:", python_data["title"])
    print("Body:", python_data["body"])
except requests.exceptions.RequestException as e:
    print("Request Failed:", e)