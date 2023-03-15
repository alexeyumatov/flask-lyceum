from requests import post, get

print("No data request -\t", post('http://127.0.0.1:5000/api/jobs', json={}).json())

print("Request without one variable -\t", post('http://127.0.0.1:5000/api/jobs',
                                               json={'job': 'test_without_id',
                                                     'work_size': 15,
                                                     'collaborators': '1, 4',
                                                     'is_finished': True}).json())

print('Request with wrong id -\t', post('http://127.0.0.1:5000/api/jobs',
                                        json={'task_id': 1,
                                              'team_leader': 2,
                                              'job': 'Success job',
                                              'work_size': 15,
                                              'collaborators': '1, 4',
                                              'is_finished': True}).json())

# Check if something accidentally was added to the database
print("All data -\t", get('http://127.0.0.1:5000/api/jobs').json())

print("Successful post request -\t", post('http://127.0.0.1:5000/api/jobs',
                                          json={'task_id': 3,
                                                'team_leader': 2,
                                                'job': 'Success job',
                                                'work_size': 15,
                                                'collaborators': '1, 4',
                                                'is_finished': True}).json())

# Checking if new data was added to the database
print("All data + added data -\t", get('http://127.0.0.1:5000/api/jobs').json())
