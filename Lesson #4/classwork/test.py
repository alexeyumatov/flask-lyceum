from requests import get

print(f'All jobs -\t{get("http://127.0.0.1:5000/api/jobs").json()}')
print(f'First job -\t{get("http://127.0.0.1:5000/api/jobs/1").json()}')
print(f'Wrong id -\t{get("http://127.0.0.1:5000/api/jobs/999").json()}')
print(f'Wrong input -\t{get("http://127.0.0.1:5000/api/jobs/s").json()}')
