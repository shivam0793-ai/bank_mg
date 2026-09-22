import requests
import json



def exists(id):

    record = {}

    if id:
        record['id'] = id

    response = requests.post(
        "http://127.0.0.1:8000/api/",
        data=json.dumps(record),
        headers={
            "Content-Type": "application/json"
        }
    )

    print("Status Code :", response.status_code)
    print("Response :", response.text)
    if response.status_code == 200:
        print(response.json())
exists(3)