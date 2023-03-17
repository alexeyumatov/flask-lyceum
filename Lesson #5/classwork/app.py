from flask_restful import Api
from flask import Flask, make_response, jsonify
from data import db_session, users_resource, jobs_resource

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/rest-api.db")
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:task_id>')
    app.run()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)



if __name__ == '__main__':
    main()
