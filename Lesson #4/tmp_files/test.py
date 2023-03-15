from requests import delete

print(delete('http://127.0.0.1:5000//api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://127.0.0.1:5000//api/news/1').json())