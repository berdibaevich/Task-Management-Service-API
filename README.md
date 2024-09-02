# Task Management System API
<hr>
<br>
<br>

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