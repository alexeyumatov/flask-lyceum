from flask import jsonify
from flask_restful import Resource, abort, reqparse
from . import db_session
from .jobs import Jobs


def abort_if_job_not_found(task_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(task_id)
    if not job:
        abort(404, message=f"User {task_id} not found")


class JobsResource(Resource):
    def get(self, task_id):
        abort_if_job_not_found(task_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(task_id)
        return jsonify({'job': job.to_dict()})

    def delete(self, task_id):
        abort_if_job_not_found(task_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(task_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs_list = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))
            for item in jobs_list]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args["team_leader"],
            job=args["job"],
            work_size=args["work_size"],
            collaborators=args["collaborators"],
            is_finished=args["is_finished"]
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
