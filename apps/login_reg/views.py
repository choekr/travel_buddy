from django.shortcuts import render, redirect
from django.contrib import messages
import re
from datetime import datetime
from .models import User
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):

  return render (request, 'login_reg/index.html')

def register(request):
  res = User.objects.register(request.POST)

  if res['added']:
    request.session['user_id'] = res['new_user'].id
    messages.success(request, "Success! Welcom, {}!".format(res['new_user'].name))
    request.session['notification'] = "Registered successfully"
    return redirect('trip0:trips')

  else:
    for error in res['errors']:
      messages.error(request, error)
    return redirect('login_reg:index')

def login(request):
  user = User.objects.login(request.POST)

  if user['access']:
    request.session['user_id'] = user['User'].id
    request.session['user_name'] = user['User'].name
    messages.success(request, "Success! Welcome, {}!".format(user['User'].name))
    request.session['notification'] = "Logged in successfully!"
    return redirect ('trip0:trips')

  else:
    messages.error(request, "Email/Password not found")
    return redirect('login_reg:index')

def logout(request):
  request.session.clear()
  messages.success(request, "Successfully logged out")
  return redirect('login_reg:index')
