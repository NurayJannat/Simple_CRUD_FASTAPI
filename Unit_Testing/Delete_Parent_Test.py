import requests


def delete_test(api_url, parent_id):
    api_url = api_url + str(parent_id)
    response = requests.delete(api_url).json()

    return response['success']


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/parents/"

    print(delete_test(api_url=api_url, parent_id=20))