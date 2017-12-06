from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import warnings
from flask.exthook import ExtDeprecationWarning

warnings.simplefilter('ignore', ExtDeprecationWarning)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final.db'

app.config.from_object('config')
db = SQLAlchemy(app)
 
from my_app.catalog.views import catalog
app.register_blueprint(catalog)
 
db.create_all()


#E:\\plac\\roadpiperassign\\