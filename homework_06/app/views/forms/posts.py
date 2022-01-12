from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("title")
    body = TextAreaField("body")


class PostEditForm(PostForm):
    id = IntegerField("id",
                      validators=[
                          DataRequired(),
                      ])
    submit_save = SubmitField(label=('Save'))


class PostListForm(PostForm):
    id = IntegerField("id",
                      validators=[
                          DataRequired(),
                      ])
    submit_delete = SubmitField(label=('Delete'))
    submit_edit = SubmitField(label=('Edit'))


class PostAddForm(FlaskForm):
    title = StringField("title",
                       validators=[
                           DataRequired(),
                           Length(max=256)
                       ])
    body = TextAreaField("body",
                           validators=[
                               DataRequired(),
                               Length(min=10)
                           ])
    submit_save = SubmitField(label=('Save'))

