""" API services """

# Utilities
import requests


def generate_request(url, params={}):
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_books(query, params={} ):

    if not query:
        return ' '''
    else:
        response = generate_request('https://www.googleapis.com/books/v1/volumes?q={}'.format(query), params)
  
    if response:
        books = response.get('items')[:10]
        return books
    
    return ' '''

def get_book (index , params={} ):

    if not index:
        return ' '''
    else:
        response = generate_request('https://www.googleapis.com/books/v1/volumes/{}'.format(index), params)
  
    if response:
        book = response.get('volumeInfo')
        return book
    
    return ' '''