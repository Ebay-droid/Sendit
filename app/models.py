from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
  __tablename__= 'users'
  
  
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique=True,index=True)
  pass_secure = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String(255))

  
  @property
  def password(self):
    raise AttributeError('You cannot reade the password attribute')
  
  @password.setter 
  def password(self, password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self, password):
    return check_password_hash(self.pass_secure,password) 
  

class Order (db.Model):
  __tablename__= 'orders'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  delivery_address= db.Column(db.String(255))
  pickup_Address = db.Column(db.String(255))
  description= db.Column(db.String(255))
  
  
