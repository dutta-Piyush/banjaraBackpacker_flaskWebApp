from flask import Flask

from .models import db
from .config import Config
from app.blueprints.create_blogs.view import create_bp
from app.blueprints.manage_blogs.view import manageBlogs_bp
from app.blueprints.create_comment.view import comment_bp
from app.blueprints.manage_comments.view import manageComments_bp


def blog_services():
    blog_service = Flask(__name__)

    # register the blueprints
    blog_service.register_blueprint(create_bp)
    blog_service.register_blueprint(manageBlogs_bp)
    blog_service.register_blueprint(comment_bp)
    blog_service.register_blueprint(manageComments_bp)

    blog_service.config.from_object(Config)

    db.init_app(blog_service)

    return blog_service
