import requests

def pad(n):
    return n # TODO: Reuse the function you wrote in lab 3!

def login_with_auth(username, password):
    r = requests.get('http://localhost/4/',
        # TODO: Update your code so that you could login with authentication without hassle!
    )
    return r

for n in range(1000):
    r = login_with_auth('admin', pad(n))
    print(n, r.text)
    if r.status_code == 200: break
    
