# Create your views here.
from django import forms
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
#from mm_test import MichealisMenten
import json

class LysoForm(forms.Form):
  initial_substrate = forms.FloatField()
  initial_enzyme = forms.FloatField()

def index(request):
  local = {}
  local.update(csrf(request))
  return render_to_response('index.html', local)

def show(request):
  lyso_form = LysoForm(request.POST)
  if lyso_form.is_valid():
    initial_substrate = lyso_form.cleaned_data['initial_substrate']
    initial_enzyme = lyso_form.cleaned_data['initial_enzyme']
  
  mm = MichealisMenten(initial_substrate, initial_enzyme)
  figure_1 = mm.kinetics()
  figure_2, figure_3 = mm.turbidity()
  
  return HttpResponse(json.dumps({
    "figure_1": figure_1,
    "figure_2": figure_2,
    "figure_3": figure_3
  }), mimetype="application/json")
