import datetime

from sqlalchemy import desc
from flask_restful import Resource, Api
from flask import Blueprint, request, jsonify, make_response

from ...models import db, Blog
from ..token_validator.token_validator import token_required

create_bp = Blueprint('create_bp', __name__)
api = Api(create_bp)


class CreateBlog(Resource):
    def get(self):
        blogs = Blog.query.order_by(desc(Blog.blog_date)).all()
        if blogs:
            # blogs_dict_list = [{'blog_id': blog.blog_id, 'blog_title': blog.blog_title,
            #                     'place_name': blog.place_name, 'author_name': blog.author_name}
            #                    for blog in blogs]
            blogs_dict_list = [{'blog_title': blog.blog_title, 'blog_body': blog.blog_body,
                                'place_name': blog.place_name}
                               for blog in blogs]
            return jsonify(blogs_dict_list)
        else:
            message = {'message': 'No blogs to display'}
            return message

    @token_required
    def post(self):
        form = request.json
        decoded_token = getattr(self, 'decoded_token', None)
        if decoded_token:
            blog_title = form.get('title')
            blog_body = form.get('body')
            place_name = form.get('place')
            author_id = decoded_token['user_id']
            author_name = decoded_token['first_name'] + ' ' + decoded_token['last_name']
            blog_date = datetime.datetime.utcnow()
            new_blog = Blog(
                blog_title=blog_title,
                blog_body=blog_body,
                place_name=place_name,
                author_id=author_id,
                author_name=author_name,
                blog_date=blog_date,
            )
            try:
                db.session.add(new_blog)
                db.session.commit()
                message = {'message': f'The new blog created by {author_name}'}
                response = make_response(jsonify(message))
                return response
            except Exception as e:
                db.session.rollback()
                message = {'message': f'Error while creating Blog - {e}'}
                response = make_response(jsonify(message))
                return response


api.add_resource(CreateBlog, '/api/create_blog')
