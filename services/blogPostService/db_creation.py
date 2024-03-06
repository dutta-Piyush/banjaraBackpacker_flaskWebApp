from app.models import db
from app import blog_services

app = blog_services()

with app.app_context():
    db.create_all()
