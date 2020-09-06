# Serverless Django on AWS Lambda

## Key Features

* ONE all-powerful button that fetches all data from USASpending.gov's Toptier Agencies endpoint and displays it on screen.

This is the future!

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Pip](https://pip.pypa.io/), and [venv](https://docs.python.org/3/library/venv.html) (to make your own serverless deployments on AWS Lambda) installed on your computer. 

### From your command line:

```bash
# Clone this repository and cd into it
$ git clone https://github.com/Javiericko/django-lambda-api.git

# Create and activate virtual environment with python 3.6 to install requirements
$ python3.6 -m venv env
$ source env/bin/activate
```

### In the "project" directory

```bash
# Install requirements
$ pip install -r requirements.txt

# Run the app
$ python manage.py runserver
```

### Open your local app

Available at http://127.0.0.1:8000/