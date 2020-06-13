from flask import Flask, redirect, render_template, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField, FileField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Regexp
import base64
import sqlite3
from config import Config
from flask_bootstrap import Bootstrap

Database = "sqlite3:///database.sql"

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

class UserForm(FlaskForm):
	user_id = DecimalField("", validators=[DataRequired()])
	email = EmailField("email", validators=[DataRequired()])
	name = StringField("Name", validators=[DataRequired()])
	sub = SubmitField("Submit")

class BeritaForm(FlaskForm):
	id_berita = DecimalField("", validators=[DataRequired()])
	title = StringField("Title", validators=[DataRequired()])
	img = FileField("Title")
	desc = TextAreaField("desciption", validators=[DataRequired()])
	us_id = DecimalField("User id", validators=[DataRequired()])
	times = DateField("Time", validators=[DataRequired()])
	sub = SubmitField("Submit")

def get_db():
	try:
		conn = sqlite3.connect(Database)

		return conn
	except Exception as e:
		print(e)

def close_db(conn):
	conn.commit()
	conn.close()

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/add-berita')
def berita():
	form = BeritaForm()
	if form.validate_on_submit():
		flash("Succesful add")
		return redirect('/home')
	return render_template("berita.html", form=form)

@app.route('/add-user')
def user():
	form = UserForm()
	if form.validate_on_submit():
		flash("Succesful add")
		return redirect('/home')
	return render_template("user.html", form=form)


if __name__ == "__main__":
	app.run(port=100)
