import requests
from datetime import datetime

USERNAME = "ceasarnjuguna"
TOKEN = "ksdjflksdjlkasdklfadsj"
GRAPH_ID = "graphczar54"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response_pixela = requests.post(url=pixela_endpoint, json=user_params)
# print(response_pixela.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graphczar54",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# authenticaiton using headers
headers = {
    "X-USER-TOKEN": TOKEN
}
# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)

# creating pixels on the graph
today = datetime.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response_pixel.text)


# updating a pixel

pixel_update = f"{pixel_endpoint}/20230423"
pixelup_config = {
    "quantity": "30.34",
}

# response_pixelup = requests.put(url=pixel_update, json=pixelup_config, headers=headers)

# deleting a pixel

response_pixeldelete = requests.delete(url=pixel_update, headers=headers)
