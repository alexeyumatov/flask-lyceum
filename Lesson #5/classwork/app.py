from flask_restful import Api
from flask import Flask
from data import db_session, users_resource

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/rest-api.db")
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:news_id>')
    app.run()


if __name__ == '__main__':
    main()
