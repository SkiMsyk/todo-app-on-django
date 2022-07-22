# What is this?
This is simple todo app on django.

# Steps

Steps to create this app.

# From basic setup to creating django project  

## Build virtual environment of Python by venv

```{shell}
$ python3 -m venv todoapp
```

Tips: Launch the venv

```{shell}
$ source todoapp/bin/activate
```

## Install Django and related libraries

Before installing Django, upgrade pip.

```{shell}
$ python -m pip install --upgrade pip
```

Create requirements.txt under root dir.

```
.
├── todoapp
│   └── ...
└── requirements.txt
```

Install libraries are wrote in `requirements.txt`.

```{shell}
$ pip install -r requirements.txt
```

## Create django project

Create django project.

```{shell}
$ django-admin startproject app
```

## Launch web server on localhost

```{shell}
$ python app/manage.py runserver
```

And then the initial page will be displayed at `http://127.0.0.1:8000` (It's depends on your env).
