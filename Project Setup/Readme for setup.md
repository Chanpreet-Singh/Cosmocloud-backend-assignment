# This Readme is specific to the project setup.
### Installation of MongoDB
Open the terminal and execute the shell script Project Setup/install_mongo.sh

> Please note that this shell script is for installing MongoDB 4.0.1 in a Debian-based machine(x86_64)

    cd Project\ Setup/; bash install_mongo.sh
We can also opt for [MongoDB Atlas](https://www.mongodb.com/atlas/database) if you don't want to set it in your local system. This doesn't require any installations of MongoDB in your local system. In that case, you must update your host in the constants file.

### Setting up Python
Make sure to create a python3.11  virtual environment as venv and install all the dependencies mentioned in [requirements](https://github.com/Chanpreet-Singh/Cosmocloud-backend-assignment/blob/main/Project%20Setup/requirements.txt) file. For this, please make sure you have python3.11 in your system and then type in<br>
`python3.11 -m venv venv`<br>
`source venv/bin/activate`<br>
`cd Project\ Setup/; pip install -r requirements.txt`

### Insertion of Dummy Data
Go to the folder: `cd Project\ Setup/custom_data/`<br>
Command: `mongoimport --db cosmocloud --collection product --file products.json  --jsonArray`
