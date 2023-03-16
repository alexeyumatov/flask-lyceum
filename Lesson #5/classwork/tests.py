from requests import get, post, delete

print('Main get -\t', get('http://127.0.0.1:5000/api/v2/users').json())

print('Get one of the users -\t', get('http://127.0.0.1:5000/api/v2/users/1').json())

print('Incorrect get -\t', get('http://127.0.0.1:5000/api/v2/users/122').json())


print('Post request -\t', post('http://127.0.0.1:5000/api/v2/users', json={'name': 'Corey',
                                                                           'about': 'CoreyCorey :)',
                                                                           'email': 'CoreyMc@mail.com'}).json())

print('Wrong post request -\t', post('http://127.0.0.1:5000/api/v2/users', json={}).json())

print('Delete request -\t', delete('http://127.0.0.1:5000/api/v2/users/3').json())

print('Wrong delete request -\t', delete('http://127.0.0.1:5000/api/v2/users/122').json())
