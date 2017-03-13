from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trip, User

# Create your views here.

def trips(request):
  if 'user_id' not in request.session:
    return redirect('login_reg:index')
  context = {
    'trips': Trip.objects.all().filter(created_user__id=request.session['user_id']) | Trip.objects.all().filter(joined_user__id=request.session['user_id']),
    'other_trips': Trip.objects.all().exclude(created_user__id=request.session['user_id']),
    'users': User.objects.get(id=request.session['user_id']),
  }
  return render(request, 'travel/index.html', context)

def add(request):
  if 'user_id' not in request.session:
    return redirect('login_reg:index')

  return render(request, 'travel/add.html')

def create(request):
  Trip.objects.create(destination=request.POST['destination'], plan=request.POST['description'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], created_user=User.objects.get(id=request.session['user_id']))
  print (request.POST['start_date'])
  # return redirect('trip0:trips')

def destination(request, id):
  context = {
    'destination': Trip.objects.filter(id=id),
    'joined_users': User.objects.filter(users__id=id)
  }
  return render (request, 'travel/view.html', context)

def join(request, id):
  join_trip = Trip.objects.get(id=id)
  additional_user = User.objects.get(id=request.session['user_id'])
  join_trip.joined_user.add(additional_user)
  return redirect('trip0:trips')
