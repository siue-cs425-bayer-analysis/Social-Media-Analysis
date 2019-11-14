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
from Twitter.views import index, searchResults

urlpatterns = [
    path('', index, name='Twitter'),
    path('search', searchResults, name='search'),
]
