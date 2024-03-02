from flask import Blueprint, render_template
from flask_restful import Api, Resource

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
@home_bp.route('/home')
def home_page():
    return render_template('home.html')
