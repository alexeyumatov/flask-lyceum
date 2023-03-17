from requests import get, post, delete

print('Main get -\t', get('http://127.0.0.1:5000/api/v2/jobs').json())

print('Get one job -\t', get('http://127.0.0.1:5000/api/v2/jobs/1').json())

print('Incorrect get -\t', get('http://127.0.0.1:5000/api/v2/jobs/122').json())

print("Successful post request -\t", post('http://127.0.0.1:5000/api/v2/jobs',
                                          json={'team_leader': 1,
                                                'job': 'TestJob post',
                                                'work_size': 14,
                                                'collaborators': '1, 2',
                                                'is_finished': True}).json())

print('Confirming post request -\t', get('http://127.0.0.1:5000/api/v2/jobs').json())

print('Wrong post request -\t', post('http://127.0.0.1:5000/api/v2/jobs', json={}).json())

print('Delete request -\t', delete('http://127.0.0.1:5000/api/v2/jobs/3').json())

print('Wrong delete request -\t', delete('http://127.0.0.1:5000/api/v2/jobs/122').json())
