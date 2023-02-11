from Create_Parent_Test import create_test as parent_create_test
from Update_Parent_Test import update_test as parent_update_test
from Delete_Parent_Test import delete_test as parent_delete_test

from Create_Child_Test import create_test as child_create_test
from Update_Child_Test import update_test as child_update_test
from Delete_Child_Test import delete_test as child_delete_test



def all_test():
    parent_api_url = "http://127.0.0.1:8000/parents/"
    child_api_url = "http://127.0.0.1:8000/child/"


    # Test 1: create parent user
    req_body = {"first_name": "Alina", "last_name": "Nitu", "address": "Lakshmi Bazar"}
    if parent_create_test(api_url=parent_api_url, req_body=req_body)==True:
        print("Test 1: Passed")

    else:
        print("Test 1: Failed")

    
    # Test 2: update parent user with wrong id
    req_body = {"first_name": "Nilu", "last_name": "Yesmin", "address": "KeraniGanj"}

    if parent_update_test(api_url=parent_api_url, parent_id=200, req_body=req_body) == False:
        print("Test 2: Passed")

    else:
        print("Test 2: Failed")

    
    # Test 3: update parent user with correct id
    req_body = {"first_name": "Nilu", "last_name": "Yesmin", "address": "KeraniGanj"}

    if parent_update_test(api_url=parent_api_url, parent_id=1, req_body=req_body) == True:
        print("Test 3: Passed")

    else:
        print("Test 3: Failed")


    # Test 4: create child user with wrong parent id
    req_body = {"first_name": "mabrur", "last_name": "ahmed", "parent_id": 200}
    if child_create_test(api_url=child_api_url, req_body=req_body)==False:
        print("Test 4: Passed")

    else:
        print("Test 4: Failed")

    
    # Test 5: create child user with correct parent id
    req_body = {"first_name": "mabrur", "last_name": "ahmed", "parent_id": 1}
    if child_create_test(api_url=child_api_url, req_body=req_body)==True:
        print("Test 5: Passed")

    else:
        print("Test 5: Failed")



    # Test 6: update child user with wrong id
    req_body = {"first_name": "jaber", "last_name": "ahmed", "parent_id": 1}

    if child_update_test(api_url=child_api_url, child_id=200, req_body=req_body) == False:
        print("Test 6: Passed")

    else:
        print("Test 6: Failed")

    
    # Test 7: update child user with correct id
    req_body = {"first_name": "jaber", "last_name": "ahmed", "parent_id": 1}

    if child_update_test(api_url=child_api_url, child_id=1, req_body=req_body) == True:
        print("Test 7: Passed")

    else:
        print("Test 7: Failed")


    # Test 8: update child user with correct id but with wrong parent_id
    req_body = {"first_name": "jaber", "last_name": "ahmed", "parent_id": 200}

    if child_update_test(api_url=child_api_url, child_id=1, req_body=req_body) == False:
        print("Test 8: Passed")

    else:
        print("Test 8: Failed")


    # Test 9: delete child user with correct id 
    if child_delete_test(api_url=child_api_url, child_id=1) == True:
        print("Test 9: Passed")

    else:
        print("Test 9: Failed")


    # Test 10: delete child user with wrong id 
    if child_delete_test(api_url=child_api_url, child_id=200) == False:
        print("Test 10: Passed")

    else:
        print("Test 10: Failed")


    # Test 11: delete parent user with wrong id 
    if parent_delete_test(api_url=parent_api_url, parent_id=200) == False:
        print("Test 11: Passed")

    else:
        print("Test 11: Failed")

    
    # Test 12: delete parent user with correct id 
    if parent_delete_test(api_url=parent_api_url, parent_id=1) == True:
        print("Test 12: Passed")

    else:
        print("Test 12: Failed")

    


if __name__ == "__main__":
    all_test()