from flask import Flask, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_supersecret_key"


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<type_list>')
def list_prof_route_handler(type_list):
    list_prof = ['пилот', 'инженер', 'строитель', 'климатолог', 'астрогеолог', 'инженер-исследователь', 'штурман',
                 'пилот дронов']
    return render_template('list_prof.html', type_list=type_list, profs=list_prof)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    information = {"title": "Анкета", "surname": "Watny", "name": "Mark", "education": "выше среднего",
                   "profession": "штурман марсохода", "sex": "male",
                   "motivation": "Всегда мечтал застрять на Марсе!", "ready": True}

    return render_template("auto_answer.html", title=information["title"], information=information)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_page.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return '<div class="success">Вы успешно вошли</div>'


@app.route('/distribution')
def distribution():
    crew = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Шон Бин']
    return render_template('distribution.html', title='Размещение по каютам', crew=crew)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
