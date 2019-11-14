from django.shortcuts import render
from django.http import HttpResponse

from .forms import redditSearchForm
from . import reddit_analysis as apiSearch

# Create your views here.
def index(request):
	form = redditSearchForm()
	return render(request, 'Reddit/reddit.html', {'form' : form})

def requestSearch(request):
	#do some things
	searchterm = request.POST.get('searchTerm', False)
	subreddit = request.POST.get('subreddit', False)
	numComments = 10
	sentimentScore = 0.05
	form = redditSearchForm
	commentsList = []

	sentimentScore, commentsList, numComments = apiSearch.prog_main(subreddit, searchterm)

	context = { 'form' : form,
	'itemSearched' : searchterm,
	'subreddit' : subreddit,
	'numComments' : numComments,
	'sentimentScore' : sentimentScore,
	'commentsList' : commentsList
	}
	return render(request, 'Reddit/reddit.html', context)
