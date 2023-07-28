from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import Length, InputRequired


class ProfileForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[Length(5, 32), InputRequired()])
    password = PasswordField("Пароль", validators=[Length(9, 24), InputRequired()])
    about_me = TextAreaField("О себе")
    submit = SubmitField("Принять")
