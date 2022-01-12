from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(80),unique=True)
    post = db.relationship("Post", back_populates="user")
    is_archive = db.Column(db.Boolean, nullable=False, default=False, server_default="FALSE")
  
    def __repr__(self):
        return f'<User {self.name}>'