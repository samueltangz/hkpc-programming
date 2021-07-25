import requests

TOKEN = '' # TODO: Paste your token here!

def get_state():
    r = requests.get('http://localhost/6/', cookies={
        'token-6': TOKEN
    })
    return r.json()

def goto_state(state):
    r = requests.post('http://localhost/6/', cookies={
        'token-6': TOKEN
    }, json={
        'state': state
    })
    return r.json()


# Go to the first state given as an option
s = get_state()
print(goto_state(s.get('options')[0]))