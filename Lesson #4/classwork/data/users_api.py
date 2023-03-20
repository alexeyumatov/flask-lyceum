import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict()
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>')
def get_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict()
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'about', 'email']):
        return jsonify({'error': 'Bad request'})
    elif db_sess.query(User).filter(User.id == request.json['id']).first():
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        name=request.json['name'],
        about=request.json['about'],
        email=request.json['email']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    required_keys = ['id', 'name', 'about', 'email']
    for key in request.json:
        if key not in required_keys:
            return jsonify({'error': 'Bad request'})
    db_sess.query(User).filter(User.id == user_id).update(request.json)
    db_sess.commit()
    return jsonify({'success': 'OK'})
