from requests import delete, get


print('Delete with wrong id -\t', delete('http://127.0.0.1:5000/api/jobs/999').json())

print('All data -\t', get('http://127.0.0.1:5000/api/jobs').json())

print('Successful delete -\t', delete('http://127.0.0.1:5000/api/jobs/3').json())

print('All data without deleted one -\t', get('http://127.0.0.1:5000/api/jobs').json())
