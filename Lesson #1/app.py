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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Отбор астронавтов</title>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
  </head>
  <body>
    <h2 align="center"> Анкета претендента</h2>
    <h3 align="center"> на участие в миссии</h3>
    <div>
        <form class="login_form" method="post">
            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
            </p>
            <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
            <div class="form-group">
                <label for="classSelect">Какое у вас образование?</label>
                <select class="form-control" id="education" name="education">
                  <option>Дошкольное</option>
                  <option>Начальное общее</option>
                  <option>Основное общее</option>
                  <option>Среднее общее</option>
                  <option>Среднее профессиональное</option>
                  <option>Высшее I степени</option>
                  <option>Высшее II степени</option>
                  <option>Высшее III степени</option>
                </select>
            </div>
            </p>
            <div class="form-group">
                <label for="form-check">Какие у Вас есть профессии?</label>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="1" value="Инженер-исследователь">
                  <label class="form-check-label" for="1">
                    Инженер-исследователь
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="2" value="Пилот">
                  <label class="form-check-label" for="2">
                    Пилот
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="3" value="Строитель">
                  <label class="form-check-label" for="3">
                    Строитель
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="4" value="Экзобиолог">
                  <label class="form-check-label" for="4">
                    Экзобиолог
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="5" value="Врач">
                  <label class="form-check-label" for="5">
                    Врач
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="6" value="Инженер по терраформированию">
                  <label class="form-check-label" for="6">
                    Инженер по терраформированию
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="7" value="Климатолог">
                  <label class="form-check-label" for="7">
                    Климатолог
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="8" value="Специалист по радиационной защите">
                  <label class="form-check-label" for="8">
                    Специалист по радиационной защите
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="9" value="Астрогеолог">
                  <label class="form-check-label" for="9">
                    Астрогеолог
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="10" value="Гляциолог">
                  <label class="form-check-label" for="10">
                    Гляциолог
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="11" value="Инженер жизнеобеспечения">
                  <label class="form-check-label" for="11">
                    Инженер жизнеобеспечения
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="12" value="Метеоролог">
                  <label class="form-check-label" for="12">
                    Метеоролог
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="13" value="Оператор марсохода">
                  <label class="form-check-label" for="13">
                    Оператор марсохода
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="14" value="Киберинженер">
                  <label class="form-check-label" for="14">
                    Киберинженер
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="15" value="Штурман">
                  <label class="form-check-label" for="15">
                    Штурман
                  </label>
                </div>

                <div class="form-check">
                  <input class="form-check-input" type="checkbox" name="prof" id="16" value="Пилот дронов">
                  <label class="form-check-label" for="16">
                    Пилот дронов
                  </label>
                </div>
            </div>
            </p>
            <div class="form-group">
                <label for="form-check">Укажите пол</label>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                  <label class="form-check-label" for="male">
                    Мужской
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                  <label class="form-check-label" for="female">
                    Женский
                  </label>
                </div>
            </div>
            </p>
            <div class="form-group">
                <label for="about">Почему Вы хотите принять участие в миссии?</label>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </div>
            </p>
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="file" name="file">
            </div>
            </p>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
            </div>
            </p>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
  </body>
</html>'''

    elif request.method == 'POST':
        print(f"Фамилия: {request.form['surname']}")
        print(f"Имя: {request.form['name']}")
        print(f"Почта: {request.form['email']}")
        print(f"Образование: {request.form['education']}")
        print(f"Профессия/Профессии: {', '.join(request.form.to_dict(flat=False)['prof'])}")
        print(f"Причина: {request.form['about']}")
        print(f"Фото: {request.form['file']}")
        print(f"Пол: {request.form['sex']}")
        print(f"Согласие: {request.form['accept']}")
        return "Форма отправлена"


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


@app.route('/carousel')
def carousel():
    return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
    rel="stylesheet" 
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
    crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"></script>
    <title>Пейзажи Марса</title>
</head>
<body>
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../static/img/mars_carousel_1.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="../static/img/mars_carousel_2.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="../static/img/mars_carousel_3.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
      </div>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
