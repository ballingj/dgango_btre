# install venv
sudo apt install python3.10-venv

# Creat virtual environment in a folded ./venv
python -m venv ./venv

# activate  -- you should see (venv) in prompt
source ./venv/bin/activate

# deactivate  -- you should see (venv) go away
deactivate

# install the pip package you need
pip install django

# ###################################
# some helpful commands             #
# ###################################

django-admin help

# start a project folder 'btre' in current directory
django-admin startproject btre .   

# 