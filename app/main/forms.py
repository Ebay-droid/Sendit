from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
# from ..models import Orders

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us abit about yourself', validators=[Required()])
  submit = SubmitField('Submit')
  
  
class OrderForm(FlaskForm):
  name = StringField('Enter your name')
  Delivery_address = StringField('Where do you want it delivered', validators=[Required()])
  pickup_address = StringField('Where will be the pickup')
  description = TextAreaField('Please describe your parcel')