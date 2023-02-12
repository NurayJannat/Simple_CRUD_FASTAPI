# Simple CRUD with FastAPI
It is a simple app that stores user data of two type: one is Parent and another child.

### User Schema
- Parent: 
    - first_name: string
    - last_name: string
    - address: string

- Child (a child user will be always under a parent user. It has one to many relation with Parent User):
    - first_name: string
    - last_name: string
    - parent_id: int

### Project Structure
It has two part. One is the main app and other is unit testing on the app.
- App: It has all endpoints of REST api to CRUD user data
- Unit testing: test the endpoints

### Installation
Create an environment with conda:
```
conda create -n <env_name> python=3.10
```

Activate the environment
```
conda activate <env_name>
```

Install dependencies
```
pip install <project_dir_path>/APP/requirements.txt
```


### Run the app
Make sure you are in project directory.
To run the app, execute the following command:
```
uvicorn APP.main:app
```

### Run Unit Testing
12 test cases have been added in unit testing. All these cases are described in **"APP/Unit_Testing/Test_cases.pdf"**
To run testing, execute this command
```
python3 Unit_Testing/All_Test.py
```
If all test case is passed, app is running..
