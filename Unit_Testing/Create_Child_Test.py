import requests


def create_test(api_url, req_body):
    response = requests.post(api_url, json=req_body).json()
    return response['success']


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/child/"

    req_body = {"first_name": "mabrur", "last_name": "ahmed", "parent_id": 16}

    print(create_test(api_url=api_url, req_body=req_body))