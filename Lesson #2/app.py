from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
