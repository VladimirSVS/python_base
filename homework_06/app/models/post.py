from .database import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False, default="", server_default="")
    body = db.Column(db.Text, nullable=False, default="", server_default="")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    user = db.relationship("User", back_populates="post")
    
    def __repr__(self):
        return f'<Post {self.title}>'