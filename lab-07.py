import time
import requests
import random
from bs4 import BeautifulSoup

TOKEN = '' # TODO: Paste your token here!

# TODO: make this function more meaningful!
def read():
    r = requests.get('http://localhost/7/', cookies={
        'token-7': TOKEN
    })
    soup = BeautifulSoup(r.text, 'html.parser')
    return [dom.get('class') for dom in soup.find_all('td', class_='game')]

def throw(x, y):
    requests.post('http://localhost/7/', cookies={
        'token-7': TOKEN
    }, json={ 'x': x, 'y': y })


# TODO: The strategy is random now. Could you devise a better strategy?
while True:
    x = random.randint(0, 99)
    y = random.randint(0, 99)

    throw(x, y)
    print('[*] Randomly threw the paintball!')
    time.sleep(10)
