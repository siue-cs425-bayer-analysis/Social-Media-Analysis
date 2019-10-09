#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:       
#   
#   Description:
#
#

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

# Create your views here.

def homeView(request, *args, **kargs):         
  if request.method == 'GET':
    form = SearchForm(request.GET)
    if form.is_valid():
      print('is valid')
    else:
      print('not clean')        
      
  else:
    return render(request, "home.html", {})
    
def search(request, *args, **kargs):
  print(request)
  return render(request, "home.html", {})
