### install venv
sudo apt install python3.10-venv

### Creat virtual environment in a folder ./venv
python -m venv ./venv

### activate  -- you should see (venv) in prompt
source ./venv/bin/activate

### deactivate  -- you should see (venv) go away
deactivate

### install the pip package you need
pip install django




### Alternative package for virtual environment

### create a virtual environment: install a package that allows to create a virtual environment
pip install virtualenv

#### now create a virtual environment with command virtualenv <name> : here we are naming env
#### this will create a new folder after the name you provided
virtualenv env

### now activate the virtual environment : you should see (env) in the front of prompt
source ./env/bin/activate

### for Windows
env\scripts\activate

### to deactivate
deactivate

### for Windows
env\scripts\deactivate


### install the package in the environment to avoid using global packages

pip install django

----------------------------------------------------------------

## some helpful commands     


### general help
django-admin help

### start a project
django-admin startproject <name_of_project>

### Ex:  start a project 'btre' in current directory
django-admin startproject btre .   

### run server
python manage.py runserver

### fix linter pylint is not installed
shift + ctrl + 'p'  # select interpreter for env
install pylint

### add the first app in current project
python manage.py startapp <name_of_app> 

### Ex: add "pages" app in btre
python manage.py startapp projects

> Note: Required step everytime you add an app:
> Go to settings.py in main project and add the new app (class name in app.py) in the INSTALLED_APPS list
> the class name is usually called 'PagesConfig'

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',
]
```