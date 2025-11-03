import requests
import json
from datetime import datetime

def getUserActivity(username):
    api_url = f"https://api.github.com/users/{username}/events"

    response = requests.get(api_url)    # guna get untuk dapatkan data from web

    if response.status_code == 200:
        # print(response.status_code)
        return response.json()
    else:
        print(f"Error {response.status_code}")
        return None
        

username=input("enter username: ") 
data = getUserActivity(username)

if data:
    for index, data in enumerate(data, start=1):
        eventType = data["type"]
        timeCreated = data["created_at"]
        formatedTime = datetime.strptime(timeCreated, "%Y-%m-%dT%H:%M:%SZ").strftime("%I:%M: %p, %d %b %Y")
        print(f"Recent activities from {username}:")
        print(f"{index}. {eventType}")
        print(f"Time created: {formatedTime}")
else:
    print("No data available. Please check username")

# print(json.dumps(data, indent=4))
# print(data[3]["actor"]["id"])