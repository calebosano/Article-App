
from flask import Blueprint,render_template
from forms import LoginForm, RegistrationForm,CreateArticleForm
from database.db_models import Users

users = Blueprint('users', __name__, template_folder='templates',
                  static_folder='static')


# Test database to render on view
@users.route('/home')
def home():
    name = Users.query.first()
    return '<h1>My name is :' + name.first_name + '</h1>'


# The user registration view
@users.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)


# The user login view
@users.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


# Creating a new article  view
@users.route('/add_article')
def add_article():
    form = CreateArticleForm()
    return render_template('add_article.html', form=form)


