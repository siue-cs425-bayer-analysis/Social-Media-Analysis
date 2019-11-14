#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:
#
#   Description:
#
#

from datetime import datetime
from django.shortcuts import render
from django.db.models import Count, Avg
from django.http import HttpResponse
import traceback

# user defined imports
#from .models import Tweet, WordList, StopWord
#from . import twittersearch as ts
#from .forms import twitterSearchForm

# Create your views here.


def index(request):
    #form = twitterSearchForm()
    return render(request, 'Reddit/reddit.html', {'form': form})


def searchResults(request):
    searchterm = request.GET['searchTerm']
    redditToSearch= request.GET['redditToSearch']
    searchError = False
    start = datetime.now()
    print('Starting Reddit Search')

    #try:
    #    ts.loadDatabase(ts.getSearchResults(searchterm, int(tweetsToget)))
    #except:
    #    searchError = True    

    print('Search complete... gathering results')

    #posTweets = Tweet.objects.values('fullText', 'sentiment').annotate(
    #    tweetCount=Count('fullText')).order_by('-sentiment')[:10]
    #negTweets = Tweet.objects.values('fullText', 'sentiment').annotate(
    #    tweetCount=Count('fullText')).order_by('sentiment')[:10]
    #common = Tweet.objects.values('fullText', 'sentiment').annotate(
    #    tweetCount=Count('fullText')).order_by('-tweetCount')[:10]
    #form = twitterSearchForm()

    #stopwords = StopWord.objects.values('stopword')
    #wordList = WordList.objects.exclude(word__in=stopwords).values(
    #    'word').annotate(count=Count('word')).order_by('-count')[:20]

    #searchMeta = { 'searchError': searchError,
    #            'searchterm': searchterm,
    #              'tweetsToget': tweetsToget,
    #              'returnCount': Tweet.objects.count(),
    #              'avgSentiment': Tweet.objects.all().aggregate(Avg('sentiment')),
    #              'numPosTweet': Tweet.objects.filter(sentiment__gt=0.05).count(),
    #              'numNegTweet': Tweet.objects.filter(sentiment__lt=-0.05).count(),
    #              'numNeuTweet': Tweet.objects.filter(sentiment__lt=0.05, sentiment__gt=-0.05).count(),
    #              'uniqueTweet': Tweet.objects.values('fullText', 'sentiment').annotate(tweetCount=Count('fullText')).order_by('-tweetCount').count()
    #              }
    print('Results gathered. Creating context')
    context = {}
    #context = {'form': form,
    #           'posTweets': posTweets,
    #           'negTweets': negTweets,
    #           'common': common,
    #           'searchMeta': searchMeta
    #           }

    print(datetime.now() - start)
    return render(request, 'Reddit/reddit.html', context)
