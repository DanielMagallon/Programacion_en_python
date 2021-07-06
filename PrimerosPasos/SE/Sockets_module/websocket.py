import requests

if __name__ == '__main__':
    url = 'https://google.com/'
    query = {'q': 'linux'}
    res = requests.get(url, data=query)
    print(res.text)