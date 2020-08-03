from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models.models import Db, User, Condo, Photo
from forms.forms import SignupForm, LoginForm, NewpostForm
from os import environ
from passlib.hash import sha256_crypt
from utils import *

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
    
@app.route('/search_page')
def search_page():
    return render_template('search.html')


@app.route('/search_page')
def search_page():
    return render_template('search.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'photo' not in request.files:
        flash('Please upload a valid image file')
        return redirect(url_for('login'))
    photo = request.files['photo']
    if not allowed_file(photo.filename):
        flash('Please upload a valid image file')
        return redirect(url_for('register'))
    form = request.form
    filtered = Condo.query
    bedsMin = form['bedsMin']
    bedsMax = form['bedsMax']
    bathsMin = form['bathsMin']
    bathsMax = form['bathsMax']
    sqftMin = form['sqftMin']
    sqftMax = form['sqftMax']
    priceMin = form['priceMin']
    priceMax = form['priceMax']
    inputZip = form['inputZip']
    if bedsMin <= bedsMax:
        filtered = filtered.filter(Condo.beds.between(bedsMin, bedsMax))
    if bathsMin <= bathsMax:
        filtered = filtered.filter(Condo.baths.between(bathsMin, bathsMax))
    if type(sqftMin) is int and type(sqftMax) is int and sqftMin <= sqftMax:
        filtered = filtered.filter(Condo.sqft.between(sqftMin, sqftMax))
    if type(priceMin) is int and type(priceMax) is int and priceMin <= priceMax:
        filtered = filtered.filter(Condo.listprice.between(priceMin, priceMax))
    if inputZip:
        filtered = filtered.filter(Condo.zip==inputZip)
    mlsnums = [condo.mlsnum for condo in filtered.limit(20).all()]
    images = Photo.query.filter(Photo.mlsnum.in_(mlsnums)).all()
    closest = findClosest(photo, images)
    session['closest'] = closest
    return redirect(url_for('results'))

@app.route('/results')
def results():
    if not 'closest' in session:
        return redirect(url_for('index'))
    closest = session['closest']
    condos = Condo.query.filter(Condo.mlsnum.in_(closest)).all()
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        return render_template('results.html', condos=condos, username=user.username)
    else:
        return render_template('results.html', condos=condos)
