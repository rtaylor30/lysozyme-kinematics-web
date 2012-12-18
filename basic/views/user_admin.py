# Create your views here.
from django import forms
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User, check_password
from django.contrib.auth.decorators import login_required
from basic.forms.user_form import UserForm, AuthorizationForm
from django.core.context_processors import csrf
from django.contrib import auth

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
    user = User.objects.create_user(username, username, password)
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

@login_required(login_url='/')
def index(request):
  if request.method != 'GET':
    return render_to_response('error_404.html')

  users = User.objects.all()
  local = {'users': users}
  local.update(csrf(request))
  return render_to_response('user/index.html', local)

def login(request):
  """
  Login the user.
  """
  form = AuthorizationForm(request.POST)
  
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/user/')
    else:
      local = {'error': 'Incorrect email/password combination'}
      local.update(csrf(request))
      return render_to_response('index.html', local)

def logout(request):
  """
  Logout the user.
  """
  auth.logout(request)
  return redirect('/')
  
def show(request, id):
  if request.method != 'GET':
    return render_to_response('error_404.html')

  return render_to_response('user/show.html')

def update(request, id):
  if request.method != 'POST':
    return render_to_response('error_404.html')

  return render_to_response('user/show.html')
