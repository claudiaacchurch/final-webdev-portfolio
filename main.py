from flask import Flask, render_template, flash, redirect
from datetime import datetime
from forms import ContactForm
from flask_ckeditor import CKEditor
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)

today = datetime.now()


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    today_year = today.strftime("%Y")
    email = os.environ.get('MY_EMAIL')
    password = os.environ.get('MY_PASSWORD')
    from_address = form.email.data
    subject = form.subject.data
    message = form.message.data
    to_address = email
    my_email = email
    my_password = password
    if form.validate_on_submit():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=from_address,
                to_addrs=to_address,
                msg=f"Subject: {subject} \n\n {message}"
            )
        flash("Email sent successfully!")
        return redirect("/#flash-message")
    return render_template("index.html", year=today_year, form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5002)