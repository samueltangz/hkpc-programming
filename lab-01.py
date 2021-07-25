import requests

def visit(page):
    r = requests.get('http://localhost/1/' + page)
    if 'Finished' in r.text: return None
    return '' # TODO: Return the URL for the next page

next_page = ''
while next_page is not None:
    next_page = visit(next_page)
    print(next_page)