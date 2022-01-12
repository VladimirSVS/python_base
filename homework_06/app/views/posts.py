from flask import Blueprint, render_template, request, redirect, url_for
from models import db, save_data, Post
from views.forms.posts import PostListForm, PostEditForm, PostAddForm
from werkzeug.exceptions import NotFound
import logger


log = logger.get_logger(__name__)

posts_app = Blueprint("posts_app", __name__)

@posts_app.route("/", methods=["GET","POST"], endpoint="posts")
def get_posts():
    posts = Post.query.order_by(Post.id).all()
    post_list_form = PostListForm()
    
    if request.method == "GET":
        if posts is None:
            raise NotFound(f'Posts Not Founds')

        return render_template(
            "posts/posts.html",
            title = 'Posts',
            posts = posts,
            form = post_list_form,
        )

    if request.method == "POST":
        log.info(f'Posts method POST success')
        log.info(f'Valivate form {post_list_form.validate_on_submit()}')
        if post_list_form.validate_on_submit():
            log.info(f'Valivate form {post_list_form.data}')
            if post_list_form.submit_edit.data:
                post = Post.query.filter_by(id = post_list_form.data['id']).first()
                return redirect(url_for("posts_app.edit"), code=307)

            if post_list_form.submit_delete.data:
                post = Post.query.filter_by(id = post_list_form.data['id']).first()
                if post is not None:
                    db.session.delete(post)
                    save_data()
                    log.info(f'Delete posts id {post.id} success')
                return redirect(url_for("posts_app.posts"))


@posts_app.route("/add/", methods=["GET","POST"], endpoint="add")
def add_posts():
    post_add_form = PostAddForm()

    if post_add_form.validate_on_submit():
        log.info(f'Validate post_add_form Ok')
        if post_add_form.submit_save.data:
            post = Post(title = post_add_form.data["title"],
                        body = post_add_form.data["body"])
            db.session.add(post)
            save_data()
        return redirect(url_for("posts_app.posts"))
    
    return render_template("posts/add.html",
                            title = 'Post Add',
                            form = post_add_form,
                            )


@posts_app.route("/edit/", methods=["GET","POST"], endpoint="edit")
def edit_posts():
    post_edit_form = PostEditForm()
    post = Post.query.filter_by(id = post_edit_form.data['id']).first()
    
    if request.method == "POST":
        log.info(f'{post_edit_form.validate_on_submit()}')
        if post_edit_form.validate_on_submit():
            if post_edit_form.submit_save.data:
                post.title = post_edit_form.data["title"]
                post.body = post_edit_form.data["body"]
                save_data()
                return redirect(url_for("posts_app.posts"))

    if hasattr(post, 'body'):
        post_edit_form.body.data = post.body
    
    return render_template("posts/edit.html",
                               title = 'Posts Edit',
                               form = post_edit_form,
                               post = post,
                               )