from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Blog(db.Model):
    blog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    blog_title = db.Column(db.String(150), nullable=True)
    blog_body = db.Column(db.Text, nullable=True)
    place_name = db.Column(db.String(20), nullable=True)
    author_id = db.Column(db.String(80), nullable=True)
    author_name = db.Column(db.String(30), nullable=True)
    blog_date = db.Column(db.DateTime, nullable=True)
    # Backref will create a column in the child db with parent as TravelBlog
    comments = db.relationship('Comment', backref='blog', cascade='all, delete-orphan')


class Comment(db.Model):
    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    comment = db.Column(db.String(100), nullable=True)
    # Write now this is manual, but once the frontend is set up,
    # take the blog id from there
    related_blog = db.Column(db.Integer, db.ForeignKey('blog.blog_id'), nullable=True)
    commenter_id = db.Column(db.String(20), nullable=True)
    commenter_name = db.Column(db.String(20), nullable=True)
    comment_date = db.Column(db.DateTime, nullable=True)


# Later you will have to deal with the issue once the user will be deleted, then logically
# blogs and comments should also be deleted. But the database are in the different services, defining a
# relationship is the main task

# Find a way to implement the logic of nested comment

# Like logic implementation
