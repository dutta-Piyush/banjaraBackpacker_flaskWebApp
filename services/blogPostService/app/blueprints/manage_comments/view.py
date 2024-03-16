import datetime

from flask_restful import Resource, Api
from flask import Blueprint, jsonify, request

from ...models import db, Comment
from ..token_validator.token_validator import token_required

manageComments_bp = Blueprint('manageComments_bp', __name__)
api = Api(manageComments_bp)


class ManageComments(Resource):
    @token_required
    def put(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            # Logic for normal user for now
            comment_obj = Comment.query.filter_by(commenter_id=decoded_token.get('user_id'),
                                                      comment_id=form.get('comment_id')).first()
            if comment_obj:
                comment_obj.comment = form.get('comment')
                try:
                    db.session.commit()
                    message = {'message': f'The comment updated! -by {comment_obj.commenter_name}'}
                    return jsonify(message)
                except Exception as e:
                    db.session.rollback()
                    message = {'message': f'Error updating blog - {e}'}
                    return jsonify(message)
            message = {'message': f'There is no such blog under your name'}
            return jsonify(message)
        else:
            message = getattr(self, 'message', None)
            return jsonify(message)

    @token_required
    def delete(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            comment = Comment.query.filter_by(commenter_id=decoded_token.get('user_id'),
                                                  comment_id=form.get('comment_id')).first()
            if comment:
                try:
                    db.session.delete(comment)
                    db.session.commit()
                    message = {'message': f'The comment deleted by - {decoded_token.get("first_name")}'}
                    return jsonify(message)
                except Exception as e:
                    db.session.rollback()
                    message = {'message': f'Error deleting blog - {e}'}
                    return jsonify(message)
            message = {'message': f'No such comment under {decoded_token.get("first_name")} name'}
            return jsonify(message)
        else:
            message = getattr(self, 'message', None)
            return jsonify(message)


api.add_resource(ManageComments, '/api/manage_comments')
