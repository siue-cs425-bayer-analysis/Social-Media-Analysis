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

from Twitter.views import twitterSearchResultsView

urlpatterns = [
    path('', twitterSearchResultsView, name='Sarch Results'),
]
        
