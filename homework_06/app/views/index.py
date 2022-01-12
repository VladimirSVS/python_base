from flask import Blueprint, render_template
from models import Post


index_app = Blueprint("index_app", __name__)

@index_app.route("/", endpoint="index")
def get_index():
    posts = Post.query.order_by(Post.id).all()
    
    return render_template("index/index.html",
                           title = 'Main',
                           posts = posts,
                           )