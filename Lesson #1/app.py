from flask import Flask, url_for, request, redirect

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


@app.route('/choice/unavailable-planet')
def show_planet():
    return "Данную планету мы не колонизируем :("


@app.route('/choice/<string:planet>', methods=['GET', 'POST'])
def choice(planet: str):
    if planet.lower() == 'марс':
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Варианты выбора</title>
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
</head>
<body>
    <h1>Мое предложение: {planet}</h1>
    <h3>Эта планета близка к Земле;</h3>
    <div class="alert alert-success" role="alert">
        На ней много необходимых ресурсов;
    </div>
    <div class="alert alert-dark" role="alert">
        На ней есть вода и атмосфера;
    </div>
    <div class="alert alert-warning" role="alert">
        На ней есть небольшое магнитное поле;
    </div>
    <div class="alert alert-danger" role="alert">
        Наконец, она просто красива!
    </div>
</body>
</html>"""
    else:
        return redirect('/choice/unavailable-planet')


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Результаты</title>
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}:</h2>
    <div class="alert alert-success" role="alert">
        <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!</h3>
    </div>
    <div class="alert alert-warning" role="alert">
        <h3>Желаем удачи!</h3>
    </div>
</body>
</html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
