import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
ID = "graph1"
USERNAME = "joyesh"
TOKEN = "haskjd32alkhdla"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
    
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":ID,
    "name":"Exercise Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers = headers)

today = datetime.now()
formated_date = today.strftime("%Y%m%d")

add_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

add_value_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "2"

}

# response = requests.post(url=add_value_endpoint,json=add_value_config,headers = headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formated_date}"
update_config = {
    "quantity":"15"
}
response = requests.put(url=update_endpoint,json=update_config,headers = headers)

print(response.text)
