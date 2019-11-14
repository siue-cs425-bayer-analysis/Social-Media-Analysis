

from django import forms


class redditSearchForm(forms.Form):
    searchTerm = forms.CharField(label="Search:", max_length=200)
    subreddit = forms.CharField(label='Subreddit to search:', max_length=200)
