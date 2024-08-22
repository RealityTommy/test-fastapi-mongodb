# fastapi-mongodb-docker-firebase
## Prerequisites
- [ ] [Python 3.12.5](https://www.python.org/downloads/release/python-3125/)
- [ ] [Docker](https://www.docker.com/)
- [ ] [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
- [ ] [MongoDB for VS Code](https://code.visualstudio.com/docs/azure/mongodb)
## How I Made This
1. Create a Python virtual environment.
```
python3 -m venv env
```
2. Activate the virtual environment.
```
source env/bin/activate
```
3. Install FastAPI.
```
pip install "fastapi[standard]"
```
4. Save dependencies.
```
pip freeze > requirements.txt
```
5. Create a `app` directory.
6. Create the following files:
	- [ ] `.env`
	- [ ] `main.py`
	- [ ] `.dockerignore`
	- [ ] `Dockerfile`
	- [ ] `docker-compose.yaml`
7. Build Docker container.
```
docker compose up --build
```
8. Run the Docker container after it has stopped.
```
docker compose up
```
## How to Set Up
1. Clone this repo.
2. Create a Python virtual environment.
```
python3 -m venv env
```
3. Activate the virtual environment.
```
source env/bin/activate
```
4. Build Docker container.
```
docker compose up --build
```
5. Run the Docker container after it has stopped.
```
docker compose up
```
## Set Up Authentication
### Firebase
Follow the following steps if you would like to use Firebase for authentication.
1. Open the [Firebase console](https://console.firebase.google.com/).
2. Click "Create a project".
	- Follow the prompts to create your new project.
3. Open the project and go to the "Authentication" module.
4. In the *Sign-in method* tab, click "Get started".
5. Enable the Sign-in providers you would like for your project.
6. Go to the project's settings (click on the gear icon in the left sidebar and click "Project settings").
7. In the *Services accounts* tab, click on "Generate new private key".
	- Name the file `serviceAccountKey.json` and save it to the following project directory: `app/config/firebase`, replacing the existing file with the same name.
8. In the *General settings* tab, go to the *Your apps* section and create a new web app.
	- Follow the prompts to create your new project.
	- On the last step, click "Continue to console"
9. In the *General settings* tab, go to the *Your apps* section and select the new web app.
10. In the *SDK setup and configuration* section, select the "Config" option and copy the dictionary values.
11. 
#### Ignore `.env`, `config.py` and `serviceAccountKey.json`
After you replace the template information in `.env`, `config.py` and `serviceAccountKey.json` with the actual values, git will see them as changes. If you are planning on pushing your project to a repo (this one or your own), **DO NOT** push your actual `.env`, `config.py` or `serviceAccountKey.json` files.

To have git ignore any changes to those files, using your terminal, navigate to the project directory and do this:
```
git update-index --assume-unchanged .env
```

```
git update-index --assume-unchanged app/config/firebase/serviceAccountKey.json
```

```
git update-index --assume-unchanged app/config/firebase/config.py
```

If you do want to track changes on this file again, do this:
```
git update-index --no-assume-unchanged .env
```

```
git update-index --no-assume-unchanged app/config/firebase/serviceAccountKey.json
```

```
git update-index --no-assume-unchanged app/config/firebase/config.py
```
## Access the Tools
* [Swagger UI](http://localhost:8000/docs)
* [ReDoc](http://localhost:8000/redoc)
* [Mongo Express](http://localhost:8081/)