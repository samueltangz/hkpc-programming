import requests

def login(username, password):
    r = requests.post('http://localhost/5/', data={
        'username': username,
        'password': password
    })
    return r.text


password = ''

cs = 'abcdefghijklmnopqrstuvwxyz0123456789-'
while True:
    for c in cs:
        # TODO: What do we need to do to recover one byte of the password?
        pass
    else:
        assert False, "done, maybe"
    print(f'[*] Password =', password)