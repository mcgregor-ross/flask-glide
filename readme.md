#### Create a virtual environment:

`python -m venv .venv`

`. .venv/bin/activate`

#### Install packages:

`pip install -r requirements.txt`

#### Run app:

`uvicorn app:app --reload --lifespan off --host 127.0.0.1 --port 8000`
