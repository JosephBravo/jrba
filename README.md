## JRBA - FastAPI - MongoDB

## Requirements 🔧

* [fastapi](https://fastapi.tiangolo.com/)
* [pymongo](https://www.mongodb.com/cloud/atlas/lp/try2?adgroup=131761122172)
* [pydantic](https://pydantic-docs.helpmanual.io/)
* [uvicorn](https://www.uvicorn.org/)
* [passlib](https://passlib.readthedocs.io/en/stable/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
* [make](https://pypi.org/project/make/)
* [pydantic[email]](https://pydantic-docs.helpmanual.io/install/)
* [bcrypt](https://pypi.org/project/bcrypt/)
* [pytest](https://docs.pytest.org/en/7.1.x/)
* [Faker](https://faker.readthedocs.io/en/master/)
* [pylint](https://pypi.org/project/pylint/)

## Installation 📌

*Clone repository and create virtual environment in project folder:*

```
python3 -m venv somename
```

## Activate environment: ▶️

- Linux:

```
source env/bin/activate
```

- Windows:

```
. env\Scripts\activate
```

## Install requirements: 🎯

- Linux:

```
make setup
```

- Windows:

```
pip install -r requirements.txt
```

## Execution - Run Project 🚀

*Located in project run command:*

- Linux:

```
make run
```

- Windows:

```
uvicorn app:app --reload
```

*This will run the application on port http://127.0.0.1:8000*

## Documentation 📋

## SwaggerUI

URL documentation: http://127.0.0.1:8000/docs#/*

## Postman

URL documentation: https://documenter.getpostman.com/view/13262243/UzBsHjMg

## Run Test [Pytest] 🔍

*Located in project run command:*

- Linux:

```
make test
```

- Windows:

```
python -m pytest
```


- Note: If you want to use the Make command in Windows, it is necessary to register the path make in environment variables.
Example in the following [link](https://parzibyte.me/blog/2020/12/30/instalar-make-windows/)
