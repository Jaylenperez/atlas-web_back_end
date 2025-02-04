from flask import Flask
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
           
@babel.localeselector
def getlocale():
    return 'en'

@app.route('/')
def index():
    return _("Hello, World!")


if __name__ == "__main__":
    app.run()
