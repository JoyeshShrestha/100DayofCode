import requests

response = requests.get("https://api.kanye.rest")

response.raise_for_status()
data = response.json()

print(data["quote"])