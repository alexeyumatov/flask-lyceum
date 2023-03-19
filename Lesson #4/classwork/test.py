from requests import put, get

print('Task #1 get -\t', get('http://127.0.0.1:5000/api/jobs/1').json())

print('Successful put -\t', put('http://127.0.0.1:5000/api/jobs/1', json={'job': 'Edited task #1', 'work_size': 15,
                                                                          'collaborators': '1, 2, 4, 7'}).json())

print('Edited Task #1 get -\t', get('http://127.0.0.1:5000/api/jobs/1').json())

print('Empty request -\t', put('http://127.0.0.1:5000/api/jobs/1', json={}).json())

print('Bad request (param "work_size" is misspelled) -\t', put('http://127.0.0.1:5000/api/jobs/1',
                                                               json={'job': 'Wrong Request',
                                                                     'work_sze': 1}).json())
