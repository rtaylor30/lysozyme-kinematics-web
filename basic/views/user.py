# Create your views here.
from django import forms
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from basic.forms.user import UserForm
from django.core.context_processors import csrf

def create(request):
  if request.method == 'GET':
    c = {}
    c.update(csrf(request))
    return render_to_response('user/new.html', c)
  
  # If this is a post request, actually create the resource.
  user_form = UserForm(request.POST)
  if user_form.is_valid():
    username = user_form.cleaned_data['username']
    password = user_form.cleaned_data['password']
    user = User(username=username, password=password)
    user.save()
    return render_to_response('user/index.html')

def delete(request, id):
  if request.method != 'POST':
    return render_to_response('error_404.html')
  
  return render_to_response('user/index.html')

def edit(request, id):
  if request.method != 'GET':
    return render_to_response('error_404.html')
  
  return render_to_response('user/edit.html')

def index(request):
  if request.method != 'GET':
    return render_to_response('error_404.html')
  
  users = User.objects.all()
  print(str(users))
  return render_to_response('user/index.html', {
    'users': users
  })
  
def show(request, id):
  if request.method != 'GET':
    return render_to_response('error_404.html')
    
  return render_to_response('user/show.html')

def sign_in(request):
  user_form = UserForm(request.POST)
  if user_form.is_valid():
    username = user_form.cleaned_data['username']
    password = user_form.cleaned_data['password']
    User.objects.filter(username=username, password=password)
  
def update(request, id):
  if request.method != 'POST':
    return render_to_response('error_404.html')
    
  return render_to_response('user/show.html')
