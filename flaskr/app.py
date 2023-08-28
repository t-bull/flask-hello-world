import os

from flask import Flask
from dotenv import load_dotenv
from .index.index import Index
from flask_sqlalchemy import SQLAlchemy

# configure environment
load_dotenv()


class App:
    db = None

    def __init__(self, config_name='default'):
        self.app = Flask(__name__, template_folder='templates')
        self.configure_app(config_name)
        self.register_blueprints()
        self.setup_extensions()

    def configure_app(self, config_name):
        postgresuri = "postgresql://{}:{}@{}:{}/{}".format(
            os.getenv('DBUSER'),
            os.getenv('POSTGRES_PASSWD'),
            os.getenv('DBHOST'),
            os.getenv('DBPORT'),
            os.getenv('DBNAME')
        )
        self.app.config["SQLALCHEMY_DATABASE_URI"] = postgresuri
        self.app.config['SQLALCHEMY_ECHO'] = True

    def setup_extensions(self):
        self.db = SQLAlchemy(self.app)
        self.init_database()

    def init_database(self):
        with self.app.app_context():
            self.db.create_all()

    def register_blueprints(self):
        index_blueprint = Index()
        self.app.register_blueprint(index_blueprint.blueprint)

    def run(self):
        self.app.run(host="0.0.0.0", port=8081, debug=True)

    def get_app(self):
        return self.app
