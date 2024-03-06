import datetime

from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify

from ...models import db, BlogComment
from ..token_validator.token_validator import token_required

comment_bp = Blueprint('comment_bp', __name__)
api = Api(comment_bp)


class CommentResource(Resource):
    def get(self):
        comment_obj = BlogComment.query.all()
        if comment_obj:
            comment_dict = [{'comment_id': cmt.comment_id, 'comment': cmt.comment,
                             'blog_id': cmt.blog_id, 'commenter_name': cmt.commenter_name,
                             'comment_date': cmt.comment_date}
                            for cmt in comment_obj]
            return jsonify(comment_dict)
        else:
            message = {'message': 'No Comment Available'}
            return jsonify(message)

    @token_required
    def post(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            comment = form['comment']
            blog_id = form['blog_id']
            commenter_id = decoded_token['user_id']
            commenter_name = decoded_token['first_name'] + ' ' + decoded_token['last_name']
            comment_date = datetime.datetime.utcnow()
            try:
                comment_obj = BlogComment(
                    comment=comment,
                    blog_id=blog_id,
                    commenter_id=commenter_id,
                    commenter_name=commenter_name,
                    comment_date=comment_date
                )
                db.session.add(comment_obj)
                db.session.commit()
                message = {'message': 'The comment is submitted'}
                return jsonify(message)
            except Exception as e:
                message = {'message': f'Error submitting the comment {e}'}
                return jsonify(message)


api.add_resource(CommentResource, '/api/write_comment')
