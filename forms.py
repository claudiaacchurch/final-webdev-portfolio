from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject")
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Send email")
