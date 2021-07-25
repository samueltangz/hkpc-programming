import requests

def login_with_cookies():
    r = requests.get('http://localhost/2/cookies/', cookies={
        # TODO: Write something here!
    })
    
    return r.text
    
def login_with_headers():
    r = requests.get('http://localhost/2/headers/', headers={
        # TODO: Write something here!
    })

    return r.text

# Do not modify the below code
if 'Welcome admin one!' in login_with_cookies():
    print('\033[032m[*] "Login with Cookies" Completed!\033[0m')
else:
    print('\033[031m[ ] "Login with Cookies" Incomplete...\033[0m')
if 'Welcome admin two!' in login_with_headers():
    print('\033[032m[*] "Login with Headers" Completed!\033[0m')
else:
    print('\033[031m[ ] "Login with Headers" Incomplete...\033[0m')