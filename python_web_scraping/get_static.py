# get static files from the internet
import requests

url = 'https://realpython.github.io/fake-jobs/'
static_data = requests.get(url)

print(static_data.text)
