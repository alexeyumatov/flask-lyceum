from flask import Flask, render_template, make_response, jsonify
from data import db_session, jobs_api, users_api


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_supersecret_key"


def main():
    db_session.global_init("db/rest-api.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='rest api')


if __name__ == '__main__':
    main()
