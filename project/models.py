from . import db, login_manager
from datetime import datetime
import hashlib
from flask import request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin

class User(UserMixin, db.Model):
	__tabelname__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable = False)
	password = db.Column(db.String(64), nullable = False)
	def __init__(self, name=None, password=None):
		self.name = name
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.name)
	def verify_password(self, password):
		return True

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
