# Serverless Django on AWS Lambda

## Key Features

* ONE all-powerful button that fetches all data from USASpending.gov's Toptier Agencies endpoint and displays it on screen.

This is the future!

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Pip](https://pip.pypa.io/), and [venv](https://docs.python.org/3/library/venv.html) (to make your own serverless deployments on AWS Lambda) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Javiericko/django-lambda-api.git

# Create and activate virtual environment with pythonn 3.6 to install requirements
$ python3.6 -m venv env
$ source env/bin/activate

# Go into the Django project
$ cd project

# Install requirements
$ pip install -r requirements.txt
```

### Setup environment variable
Now, you will need to set the Django Secret Key for the app to run. In your text editor:
* You can generate your own 50 character key yourself or on a site like [this](https://miniwebtool.com/django-secret-key-generator/).
* Open the file ".env.example" under project/project.
* Replace the XXXXXXXX placeholder for your generated key. ->Make sure to keep the quotation marks.<-
* Rename ".env.example" to ".env".

### Run the app
```bash
$ python manage.py runserver
```