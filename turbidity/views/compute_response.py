# Create your views here.
from django import forms
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def delete(request, id):
  if request.method != 'POST':
    return render_to_response('error_404.html')
  
  return render_to_response('compute_response/index.html')

def edit(request, id):
  if request.method != 'GET':
    return render_to_response('error_404.html')
  
  return render_to_response('compute_response/edit.html')

def index(request):
  if request.method != 'GET':
    return render_to_response('error_404.html')
  
  return render_to_response('compute_response/index.html')
  
def show(request, id):
  if request.method != 'GET':
    return render_to_response('error_404.html')
    
  return render_to_response('compute_response/show.html')
  
def update(request, id):
  if request.method != 'POST':
    return render_to_response('error_404.html')
    
  return render_to_response('compute_response/show.html')

