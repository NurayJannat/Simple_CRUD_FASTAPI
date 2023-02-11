import requests


def update_test(api_url, child_id, req_body):
    api_url = api_url + str(child_id)
    response = requests.put(api_url, json=req_body).json()
    return response['success']


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/child/"

    req_body = {"first_name": "jaber", "last_name": "ahmed", "parent_id": 16}

    print(update_test(api_url=api_url, child_id=4, req_body=req_body))