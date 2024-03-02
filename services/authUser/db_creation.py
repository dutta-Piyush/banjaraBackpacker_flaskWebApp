from app.model import db
from app import auth_service

app = auth_service()

with app.app_context():
    db.create_all()
