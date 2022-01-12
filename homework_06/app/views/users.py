from flask import Blueprint, render_template, request, redirect, url_for
from models import db, save_data, User
from views.forms.users import UserListForm, UserEditForm, UserAddForm
from werkzeug.exceptions import NotFound
import logger


log = logger.get_logger(__name__)

users_app = Blueprint("users_app", __name__)

@users_app.route("/", methods=["GET","POST"], endpoint="users")
def get_users():
    users = User.query.filter(User.is_archive == False).order_by(User.id).all()
    user_list_form = UserListForm()
    
    if request.method == "GET":
        if users is None:
            log.error(f'Users Not Founds')
            raise NotFound(f'Users Not Founds')

        return render_template(
            "users/users.html",
            title = 'Users',
            users = users,
            form = user_list_form,
        )

    if request.method == "POST":
        if user_list_form.validate_on_submit():
            if user_list_form.submit_edit.data:
                user = User.query.filter_by(id = user_list_form.data['id']).first()
                return redirect(url_for("users_app.edit"), code=307)

            if user_list_form.submit_delete.data:
                user = User.query.filter_by(name = user_list_form.data['name']).first()
                if user is not None:
                    db.session.delete(user)
                    save_data()
                return redirect(url_for("users_app.users"))


@users_app.route("/add/", methods=["GET","POST"], endpoint="add")
def add_users():
    user_add_form = UserAddForm()

    if user_add_form.validate_on_submit():
        log.info(f'Validate user_add_form Ok')
        if user_add_form.submit_save:
            user = User(name = user_add_form.data["name"],
                        username = user_add_form.data["username"],
                        email = user_add_form.data["email"])
            db.session.add(user)
            save_data()
        return redirect(url_for("users_app.users"))
    
    return render_template("users/add.html",
                            title = 'User Add',
                            form = user_add_form,
                            )


@users_app.route("/edit/", methods=["GET","POST"], endpoint="edit")
def edit_users():
    user_edit_form = UserEditForm()
    user = User.query.filter_by(id = user_edit_form.data['id']).first()
    if request.method == "POST":
        if user_edit_form.validate_on_submit():
            if user_edit_form.submit_save.data:
                user.name = user_edit_form.data["name"]
                user.username = user_edit_form.data["username"]
                user.email = user_edit_form.data["email"]
                save_data()
                return redirect(url_for("users_app.users"))

    return render_template("users/edit.html",
                               title = 'User Edit',
                               form = user_edit_form,
                               user = user,
                               )
