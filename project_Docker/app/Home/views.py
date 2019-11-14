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

#from .forms import NameForm

# Create your views here.

def homeView(request, *args, **kargs):         

    return render(request, 'Home/dashboard.html', {})
    
