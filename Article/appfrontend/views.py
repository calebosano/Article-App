
from flask import Blueprint,render_template
from database.db_models import Users

articles = Blueprint('articles', __name__, template_folder='templates',
                     static_folder='static')


# Test database to render on view
@articles.route('/home')
def home():
    name = Users.query.first()
    return render_template('home.html', name=name)





