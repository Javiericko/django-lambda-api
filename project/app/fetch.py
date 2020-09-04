import requests

# import function to run
def fetch(url):
    r = requests.get(url).json()
    return r