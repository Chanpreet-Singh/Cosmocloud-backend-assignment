# Cosmocloud-backend-assignment
This project contains code, as an assignment, completed as a part of the hiring process of Cosmocloud. Details about the assignment can be found [here](https://github.com/Chanpreet-Singh/Cosmocloud-backend-assignment/blob/main/Assignment%20Task.pdf).

### Development environment:
- [Debian/Ubuntu 20.04 LTS](https://releases.ubuntu.com/focal/ "Debian/Ubuntu 20.04 LTS")
- [Python 3.11](https://www.python.org/downloads/release/python-3117/)
- [Fast API Service](https://fastapi.tiangolo.com/ "Fast API Service")
- [MongoDB 5.0.24](https://www.mongodb.com/docs/v5.0/release-notes/5.0/)

### Setting up of the project
Follow this [readme document](https://github.com/Chanpreet-Singh/Cosmocloud-backend-assignment/blob/main/Project%20Setup/Readme%20for%20setup.md) to set up the project.

### Deployment
The project was deployed in the local development machine. However, it can also be deployed in a cloud-based VM using NGINX or Apache Servers.

### Execution
- Activate the virtual environment: `source venv/bin/activate`
- Go to the folder: `cd backend`<br>
- Command to execute the API: `uvicorn api:app --reload`

### Explanation of scripts
- ***api.py***: This is the main script that acts as the entry point to the API. Also, in here connection to the database is defined via mongo_utils.
- ***api_helper.py***: This is the helper script to the main script i.e. all the API logic is written in here. It interacts with the database via mongo_utis.
- ***mongo_utils.py***: In this script, the basic CRUD(only required in the project) operations using pymongo library are written.
- ***constants.py**: This file contains the database credentials, ideally it should be in a secure vault/file. 
- ***models.py***: In this python file, the request's payload's model of the second API is kept so that Fast API Service automatically validates it.
