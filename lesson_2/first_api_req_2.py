import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

try:
    response = requests.get(url)
    response.raise_for_status()
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("Title:", data["title"])
        print("Body:", data["body"])
    else:
        print("Request Failed.")
except requests.exceptions.RequestException as e:
    print("An error occured:", e)
