#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:       
#   
#   Description:
#
#

from django .urls import path
from Home.views import homeView 

urlpatterns = [
    path('',homeView, name='Home'),
    path('homeView', homeView, name='Home'),
]
   
