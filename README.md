# Task Management System API


# Installation

```bash
$ git clone https://github.com/berdibaevich/Task-management-service-API.git
$ cd project
$ pip install -r requirements.txt
$ cd task_management
$ python manage.py make migrations
$ python manage.py migrate
$ python manage.py runserver
```

# Setting Up Environment Variables
To securely manage sensitive data such as the Django <b>SECRET_KEY</b> and <b>database</b> credentials, you'll need to create a <b>.env</b> file inside the <b>task_management</b> folder.
```
SECRET_KEY="YOUR KEY"
DEBUG=True

POSTGRES_DB=DATABASE_NAME
POSTGRES_USER=USER_NAME
POSTGRES_PASSWORD=PASSWORD
POSTGRES_HOST=HOST_NAME
```


# Project structure                                                     

```
[project]
├── docker
│   ├── docker-compose.yml
│   └── Dockerfile
├── task_management
│   ├── apps
│   │   └── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── tests
│   │   └── __init__.py
│   ├── conftest.py
│   ├── pytest.ini
│   └── manage.py
├── .gitignore
├── README.md
└── requirements.txt
