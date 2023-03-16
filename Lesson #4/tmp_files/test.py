from requests import post

print(post('http://127.0.0.1/api/jobs',
           json={'team_leader': 1,
                 'job': 'test123',
                 'work_size': 15,
                 'collaborators': '1, 4',
                 'is_finished': False}).json())
