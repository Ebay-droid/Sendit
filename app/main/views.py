from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User
from .forms import UpdateProfile,OrderForm

@main.route('/')
def index():
  
  return render_template('index.html')

@main.route('/user/<username>')
def profile(username):
  user = User.query.filter_by(username=username).first()
  user_id = current_user.id
  user = current_user
  
  if user is None:
    abort(404)
    
  return render_template('profile/profile.html')

@main.route('/user/<username>/update')
@login_required
def update_profile(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    abort (404)
    
  form = UpdateProfile()
    
  if form.validate_on_submit():
      user.bio =form.bio.data
      
      db.session.add(user)
      db.session.commit()
      
      return  redirect(url_for('.profile', username=username))
  
  return render_template('profile/update_profile.html', form=form)    