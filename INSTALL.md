# Installation Instructions
______________________________

### What I did

1. Install Python and Django or use an IDE such as Pycharm
2. Make a new project directory and virtual environment
3. Run: ```pip install -r requirements.txt```
4. Create project: ```django-admin startproject GOvetproject```
5. Create application: ```django-admin startapp urlshort```
6. Install application in settings.py: ```INSTALLED_APPS = [... appname.urlshort]```
7. Move SECRET_KEY to secrets.py and add to .gitignore
8. Import views and project folder files in urls.py
9.	Test the webserver: ```python manage.py runserver 8000```
10. 10.	Do the migration and initialize database: ```python manage.py migrate```
11. Create an admin account to access the backend: ```python manage.py createsuperuser```

### What you have to do

