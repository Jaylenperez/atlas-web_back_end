from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
           
def get_locale():
    """
    Returns the best match for a supported locale based on the 'Accept-Language'
    header in the incoming requests.
    
    Returns:
        str: The best match language code ('en' or 'fr').
    """
    return request.accept_languages.best_match(['en', 'fr'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    """
    Returns translated message based on client's locale.

    Returns:
        str: Translated greeting message.
    """
    return _("Hello, World!")


if __name__ == "__main__":
    app.run()
