# fastapi-docker
## Prerequisites
- [ ] [Python 3.12.5](https://www.python.org/downloads/release/python-3125/)
- [ ] [Docker](https://www.docker.com/)
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
## Access the Tools
* [Swagger UI](http://localhost:8000/docs)
* [ReDoc](http://localhost:8000/redoc)
* [Mongo Express](http://localhost:8081/)