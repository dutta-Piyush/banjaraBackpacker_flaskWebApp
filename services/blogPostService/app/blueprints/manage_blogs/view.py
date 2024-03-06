import datetime
from flask_restful import Resource, Api
from flask import Blueprint, jsonify, request

from ...models import db, TravelBlog
from ..token_validator.token_validator import token_required

manageBlogs_bp = Blueprint('manageBlogs_bp', __name__)
api = Api(manageBlogs_bp)


class ManageBlogs(Resource):
    @token_required
    def put(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        # Logic for normal user for now
        if decoded_token:
            blog = TravelBlog.query.filter_by(author_id=decoded_token.get('user_id'),
                                              blog_id=form.get('blog_id')).first()
            if blog:
                author_name = decoded_token['first_name'] + ' ' + decoded_token['last_name']
                blog.blog_title = form.get('blog_title', blog.blog_title)
                blog.blog_body = form.get('blog_body', blog.blog_body)
                blog.place_name = form.get('place_name', blog.place_name)
                blog.author_id = decoded_token['user_id']
                blog.author_name = decoded_token['first_name'] + ' ' + decoded_token['last_name']
                blog.blog_date = datetime.datetime.utcnow()
                try:
                    db.session.commit()
                    message = {'message': f'The blog updated! -by {author_name}'}
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
            blog = TravelBlog.query.filter_by(author_id=decoded_token.get('user_id'),
                                              blog_id=form.get('blog_id')).first()
            if blog:
                try:
                    db.session.delete(blog)
                    db.session.commit()
                    message = {'message': f'The blog deleted by - {decoded_token.get("first_name")}'}
                    return jsonify(message)
                except Exception as e:
                    db.session.rollback()
                    message = {'message': f'Error deleting blog - {e}'}
                    return jsonify(message)
            message = {'message': f'No such blog under {decoded_token.get("first_name")} name'}
            return jsonify(message)
        else:
            message = getattr(self, 'message', None)
            return jsonify(message)


api.add_resource(ManageBlogs, '/api/manage_blogs')
