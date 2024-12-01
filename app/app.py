from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Base
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager()
login.init_app(app)
login.login_view = 'auth.login'

from ingredient import bp as ingredient_bp
app.register_blueprint(ingredient_bp, url_prefix='/ingredient')
from auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')


@app.route('/')
def hello_world():  # put application's code here
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
