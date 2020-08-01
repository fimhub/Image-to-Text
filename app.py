from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models.models import Db, User, Condo, Photo
from forms.forms import SignupForm, LoginForm, NewpostForm
from os import environ
from passlib.hash import sha256_crypt

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:HCMCTWAG@1@localhost/img2txt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = environ.get('SECRET_KEY')
Db.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    # Control by login status
    if 'username' in session:
        session_user = User.query.filter_by(username=session['username']).first()
        return render_template('index.html', title='Home', session_username=session_user.username)
    else:
        return render_template('index.html', title='Home')


#GET & POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Init form
    form = LoginForm()

    # If post
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user by Db query
        user = User.query.filter_by(username=username).first()

        # Control login validity
        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username
            return redirect(url_for('index'))

    # If GET
    else:
        return render_template('login.html', title='Login', form=form)


#GET & POST /signup
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Init form
    form = SignupForm()

    # IF POST
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user from Db query
        existing_user = User.query.filter_by(username=username).first()

        # Control new credentials
        if existing_user:
            flash('The username already exists. Please pick another one.')
            return redirect(url_for('register'))
        else:
            user = User(username=username, password=sha256_crypt.hash(password))
            Db.session.add(user)
            Db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))

    # IF POST
    else:
        return render_template('register.html', title='register', form=form)


#GET & POST /newpost
@app.route('/newimage', methods=['GET', 'POST'])
def newimage():
    # Init form
    form = NewpostForm()

    # If POST
    if request.method == 'POST':

        # Init user from poster
        session_user = User.query.filter_by(username=session['username']).first()

        # Init content from form request
        content = request.form['content']

        # Create in DB
        new_post = Post(author=session_user.uid, content=content)
        Db.session.add(new_post)
        Db.session.commit()
        

        return redirect(url_for('index'))

    # If GET
    else:
        return render_template('newimage.html', title='Newpost', form=form)
