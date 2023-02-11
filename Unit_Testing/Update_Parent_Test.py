import requests


def update_test(api_url, parent_id, req_body):
    api_url = api_url + str(parent_id)
    response = requests.put(api_url, json=req_body).json()

    return response['success']


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/parents/"

    req_body = {"first_name": "Nilu", "last_name": "Yesmin", "address": "KeraniGanj"}

    print(update_test(api_url=api_url, parent_id=20, req_body=req_body))