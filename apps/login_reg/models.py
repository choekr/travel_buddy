from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import re, bcrypt

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')
# Create your models here.
class UserManager(models.Manager):
  def register(self, data):

    errors = []
    response = {}

    if len(data['username' and 'name' and 'password' and 'confirm_pw'])<1:
      errors.append("You cannot leave any  field blank!")
    elif len(data['name'])<3:
      errors.append("Your name must be longer than 3 characters")
    elif not (data['name']).replace(' ','').isalpha():
      errors.append("Your name can only contain letters")
    elif not USERNAME_REGEX.match(data['username']):
      errors.append("Username may not contain anything else than alphabets and numbers")
    elif len(data['password'])<8:
      errors.append("Password must be at least 8 characters long")
    elif not (data['password']==data['confirm_pw']):
      errors.append("Unable to confirm password. Please enter same password you have entered above")

    if not errors:
      password = data['password'].encode()
      hashed = bcrypt.hashpw(password, bcrypt.gensalt())
      new_user = self.create(name=data['name'], username=data['username'], password=hashed)
      response['added'] = True
      response['new_user'] = new_user


    else:
      response['added'] = False
      response['errors'] = errors

    print (errors)

    return response

  def login(self, data):
    response = {}

    user = User.objects.filter(username=data['username'])

    if user:
      user = user[0]
      pw = data['login_pw'].encode()

      if bcrypt.hashpw(pw, user.password.encode()) == user.password.encode():

        response['access'] = True
        response['User'] = user
      else:
        response ['access'] = False
    else:
      response['access'] = False
    return response




class User(models.Model):
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
