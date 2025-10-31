import requests
import json

def getUserActivity():
    api_url = "https://api.github.com/users/syauu/events"

    response = requests.get(api_url)    # gune get untuk dapatkan data from web

    if response.status_code == 200:
        return response.json()
    
data = getUserActivity()
print(json.dumps(data, indent=4))