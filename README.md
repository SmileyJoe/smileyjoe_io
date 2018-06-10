# smileyjoe_io #

Django project for personal website [smileyjoe.io](http://smileyjoe.io)

## Apps ##

### Secret ###

Secret is a simple way of sharing one time use data. This can be used for sending a passowrd over an email 
for example.

#### How it works ####

The secret is entered into the input field, a 1 time use unique url is generated which can be shared with
anyone. Once this link is opened, the secret will be displayed on the screen and then permanently deleted
from the website. All secrets, viewed or not, will be removed after 72 hours.

## Setup ##

1. Create the following environment variables:
- `SMILEYJOE_IO_SECRET_KEY` - The Django secret key.
- `SMILEYJOE_IO_DEBUG` - Whether to run in the debug environment or not.
- `SMILEYJOE_IO_PARENT_HOST` - The main domain where the project will be hosted, eg, `localhost:8000`
- `SMILEYJOE_IO_GA` - Google analytics code
2. Install [MiniConda](https://conda.io/miniconda.html)
3. Create the virtual environment with `conda create --name <env> --file requirements.txt`
4. Run the project with `python manage.py runserver`

## Branch Naming ##

- `master` - What is currently released
- `develop` - Code that is ready for released
- `app_<app_name>` - Start of a new app
- `feature_<app_name>_<feature_name>` - New feature to a specific app
- `fix_<feature_name>_<short_description>` - Fix to a specific feature
- `fix_<app_name>_<short_description>` - Fix to a specific app
- `fix_<short_description>` - A general fix that effects the whole site