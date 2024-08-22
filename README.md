# medisense_backend
a project for capture data for therapeutics and ergonomical purposes


## Setting Up

### Create env
```shell
conda create --name <PROEJCT NAME> python=3.10
```

```shell
conda activate <PROEJCT NAME>
```

### Install dependencies
```shell
pip install -r requiriments.txt
```

## ENV
Create .env on core folder with the next data
```shell
ENV = development

DB_URL = <<DB URL>>
DB_PORT = <<DB PORT>>
DB_NAME = <<DB NAME>>
DB_PWD = <<DB PASSWORD>>
DB_USR = <<DB USER>>

SECRET_KEY = <<SECRET KEY>>
REFRESH_SECRET_KEY = <<REFRESH TOKEN SECRET KEY>>
ALGORITHM = <<ALGORITHM>>
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1800
TIMEOUT = 60

```

## Setup Alembic
### create directory versions
```shell
cd alembic 
mkdir versions
```
### Generate Initial Migration
```shell
alembic revision --autogenerate -m "Initial migration"
```

### Apply Migrations
```shell
alembic upgrade head
```

## Run the test
```shell
python -m unittest .\app\test\<TEST_NAME>.py
```

## Run the Application

### uvicorn (Best Option)
```shell
uvicorn app:app --reload
```

### Python
```shell
fastapi dev app
```
