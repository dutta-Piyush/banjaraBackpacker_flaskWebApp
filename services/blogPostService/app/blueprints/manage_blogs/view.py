import datetime
from sqlalchemy import desc
from flask_restful import Resource, Api
from flask import Blueprint, jsonify, request, make_response

from ...models import db, Blog
from ..token_validator.token_validator import token_required

manageBlogs_bp = Blueprint('manageBlogs_bp', __name__)
api = Api(manageBlogs_bp)


class ManageBlogs(Resource):

    @token_required
    def get(self):
        decoded_token = getattr(self, 'decoded_token', None)
        blogs = Blog.query.filter_by(author_id=decoded_token.get('user_id')).order_by(desc(Blog.blog_date)).all()
        if decoded_token:
            blogs_dict = [{'blog_id': blog.blog_id, 'blog_title': blog.blog_title, 'blog_body': blog.blog_body,
                           'place_name': blog.place_name, 'author_name': blog.author_name,
                           'blog_date': blog.blog_date}
                          for blog in blogs]
            message = {"message": "All the user's blogs"}
            response_data = {'blogs_dict': blogs_dict, 'message': message}
            response = make_response(response_data)
            response.status_code = 200
            return response
        else:
            message = getattr(self, 'message', None)
            response = make_response(message)
            response.status_code = 401
            return response

    @token_required
    def put(self):
        form = request.json
        print("Form", form)
        decoded_token = getattr(self, 'decoded_token', None)
        # Logic for normal user for now
        if decoded_token:
            blog = Blog.query.filter_by(author_id=decoded_token.get('user_id'),
                                        blog_id=form.get('blogId')).first()
            print("Blog", blog)
            # print(" ID ", blog.get('blog_id'))
            # print(" Title ", blog.get('blog_title'))
            if blog:
                author_name = decoded_token['first_name'] + ' ' + decoded_token['last_name']
                blog.blog_title = form.get('blogTitle', blog.blog_title)
                blog.blog_body = form.get('blogBody', blog.blog_body)
                blog.place_name = form.get('placeName', blog.place_name)
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
            response = make_response(message)
            response.status_code = 200
            return response
        else:
            message = getattr(self, 'message', None)
            response = make_response(message)
            response.status_code = 401
            return response

    @token_required
    def delete(self):
        print("inside the delete")
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token and form:
            blog = Blog.query.filter_by(author_id=decoded_token.get('user_id'),
                                        blog_id=int(form.get('blog_id'))).first()
            if blog:
                try:
                    db.session.delete(blog)
                    db.session.commit()
                    message = {'message': f'The blog {blog.blog_title} deleted by - {decoded_token.get("first_name")}'}
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
