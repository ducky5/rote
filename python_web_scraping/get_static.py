# get static files from the internet
import requests

url = 'https://realpython.github.io/fake-jobs/'
static_data = requests.get(url) #get request

# show headers
print(static_data.headers)


print(static_data.text)
