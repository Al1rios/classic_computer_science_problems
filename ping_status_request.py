import requests

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.status_code}')

urls = [
    'https://www.terra.com',
    'http://httpstat.us/200',
    ]

for url in urls:
    ping(url)

print('Done.')