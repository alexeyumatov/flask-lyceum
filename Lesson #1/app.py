from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion():
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport">
    <title>Колонизация Марса</title>
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
    crossorigin="anonymous">
    <link rel="stylesheet" href={url_for('static', filename='css/style.css')}>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img style="width: 33%;" src="{url_for('static', filename='img/mars.png')}">
    <figcaption>Вот она какая, красная планета.</figcaption>

    <div class="alert alert-dark" role="alert">
        Человечество вырастает из детства.
    </div>
    
    <div class="alert alert-success" role="alert">
        Человечеству мала одна планета.
    </div>
    
    <div class="alert alert-dark" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    
    <div class="alert alert-warning" role="alert">
        И начнем с Марса!
    </div>

    <div class="alert alert-danger" role="alert">
        Присоединяйся!
    </div>
</body>
</html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return """"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
