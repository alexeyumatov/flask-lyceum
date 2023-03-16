from flask_restful import Resource, abort
from .users import User
from . import db_session


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users_list = session.query(User).get(user_id)
        return jsonify({'users': users_list.to_dict(
            only=('name', 'about', 'email'))})

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users_list = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'about', 'email')) for item in users_list]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = users.User(
            name=args["name"],
            about=args["about"],
            email=args["email"]
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
