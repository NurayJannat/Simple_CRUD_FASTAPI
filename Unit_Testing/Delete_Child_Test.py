import requests


def delete_test(api_url, child_id):
    api_url = api_url + str(child_id)
    response = requests.delete(api_url).json()

    return response['success']


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/child/"

    print(delete_test(api_url=api_url, child_id=4))