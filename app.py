from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport">
    <title>Колонизация Марса</title>
</head>
<body>
    <p>Человечество вырастает из детства.</p>

    <p>Человечеству мала одна планета.</p>

    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>

    <p>И начнем с Марса!</p>

    <p>Присоединяйся!</p>
</body>
</html>"""


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс!</h1>
    <img style="width: 33%;" src="{url_for('static', filename='img/mars.png')}">
    <figcaption>Вот она какая, красная планета.</figcaption>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
