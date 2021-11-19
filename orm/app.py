from flask import Flask
from flask.app import _Body
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:teste123456@localhost/aula05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    info = db.Column(db.String(128))

    def json(self):
        return {'id': self.id, 'name': self.name}

class Post(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationShip('Category', backref=db.backref('posts', lazy=True))
    user_id = db.Column(db.Intenger, db.ForeignKey('user.id'))
    user = db.Relationship('User', backref=db.backref('users', lazy=True))

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'category_id': self.category_id,
            'category': self.category.name,
            'user_id': self.user_id,
            'user': self.user.name
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name}    

