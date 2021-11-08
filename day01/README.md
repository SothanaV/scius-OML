# Day 01

- virtualenv 

```
# create
virtualenv <ENV NAME>

# use
source ./env/bin/activate
```

- install django
```
pip install django
```

- start project
```
django-admin startproject <PROJECT-NAME>
```

- start app
```
python manage.py startapp <APP-NAME>
```

- database operation
```
# run first prepair migrate database
python manage.py makemigrations

# real migrate database
python manage.py migtate
```

- create superuser
```
python manage.py createsuperuser
```

- runserver
```
python manage.py runserver
```