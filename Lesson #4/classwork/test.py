from requests import put, get, post, delete

# GET REQUESTS

print('Get request \t-\t', get('http://127.0.0.1:5000/api/users').json())

print('Get one item \t-\t', get('http://127.0.0.1:5000/api/users/1').json())

print('Wrong get request \t-\t', get('http://127.0.0.1:5000/api/users/123').json(), '\n\n')

# PUT REQUESTS
print('Wrong put request (param "email" is misspelled) \t-\t',
      put('http://127.0.0.1:5000/api/users/1', json={'emil': 'alex@ya.ru'}).json())

print('Empty put request \t-\t', put('http://127.0.0.1:5000/api/users/1', json={}).json())

print('Edit user email \t-\t', put('http://127.0.0.1:5000/api/users/1', json={'email': 'alex@ya.ru'}).json())

print('Checking updates \t-\t', get('http://127.0.0.1:5000/api/users/1').json(), '\n\n')

# POST REQUESTS
print('Empty post request \t-\t', post('http://127.0.0.1:5000/api/users', json={}).json())

print('Wrong post request \t-\t', post('http://127.0.0.1:5000/api/users', json={'id': 4,
                                                                                'name': 'Dylan'}).json())

print('Post request \t-\t', post('http://127.0.0.1:5000/api/users', json={'id': 4,
                                                                          'name': 'Dylan',
                                                                          'about': 'My name is Dylan. Hi!',
                                                                          'email': 'DylanDylan@gmail.com'}).json())

print('Checking updates \t-\t', get('http://127.0.0.1:5000/api/users/4').json(), '\n\n')

# DELETE REQUESTS
print('Wrong delete request \t-\t', delete('http://127.0.0.1:5000/api/users/1313').json())

print('Delete request \t-\t', delete('http://127.0.0.1:5000/api/users/2').json())

print('Checking updates \t-\t', get('http://127.0.0.1:5000/api/users').json())
