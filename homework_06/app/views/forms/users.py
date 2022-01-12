from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField("name",
                       validators=[
                           DataRequired(),
                           Length(max=40)
                       ])
    username = StringField("username",
                           validators=[
                               DataRequired(),
                               Length(max=50)
                           ])
    email = StringField("email", 
                        validators=[
                            DataRequired(),
                            Email(),
                            Length(max=80)
                            ])


class UserEditForm(UserForm):
    id = IntegerField("id",
                      validators=[
                          DataRequired(),
                      ])
    submit_save = SubmitField(label=('Save'))


class UserListForm(UserForm):
    id = IntegerField("id",
                      validators=[
                          DataRequired(),
                      ])
    submit_delete = SubmitField(label=('Delete'))
    submit_edit = SubmitField(label=('Edit'))


class UserAddForm(UserForm):
    submit_save = SubmitField(label=('Save'))

