
from flask import Flask
from config import FLASK_DEBUG

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=FLASK_DEBUG)


