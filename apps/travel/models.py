from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User
from datetime import datetime

# Create your models here.
class TripManager(models.Manager):
  def validation(self, data):
    now = datetime.datetime.now()
    errors=[]

    if not data['destination']:
      errors.append('Please enter your destination')
    if not data['start_date']:
      errors.append('Please enter the start date for your trip')
    if not data['end_date']:
      errors.append('Please enter the ending date for your trip')
    if data['start_date']>data['end_date']:
      errors.append('You cannot end your trip before it begins')
    if data['start_date'] < str(now):
      errors.append('Please enter a valid start date for your trip')
    if data['end_date'] < str(now):
      errors.append('Please enter a valid end date for your trip')

    response = {}
    if not errors:
      response['add'] = True
      return response

    else: 
      response['add'] = False
      response['errors'] = errors
      return response

class Trip(models.Model):
  destination = models.CharField(max_length=255)
  plan = models.CharField(max_length=255)
  start_date = models.DateField()
  end_date = models.DateField()
  created_user = models.ForeignKey(User)
  joined_user = models.ManyToManyField(User, related_name='users')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TripManager()
