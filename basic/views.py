# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mm_test import MichealisMenten

def index(request):
  return render_to_response('index.html')

def show(request, s, v):
  print s
  print v
  mm = MichealisMenten(float(s), float(v))
  figure_1 = mm.kinetics()
  figure_2, figure_3 = mm.turbidity()
  
  return render_to_response('charts.html', {'image_1': figure_1, 'image_2': figure_2, 'image_3': figure_3});
