#  How do you structure a Flask app using Blueprints?

from flask import Flask
from blueprints.auth.routes import auth_bp
from blueprints.dashboard.routes import dashboard_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')


if __name__ == '__main__':
    app.run(debug=True)