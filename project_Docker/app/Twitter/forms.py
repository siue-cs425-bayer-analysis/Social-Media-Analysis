

from django import forms

class twitterSearchForm(forms.Form):
	searchTerm = forms.CharField(label="Search", max_length=200)
	tweetsToreturn = forms.IntegerField(label='Number Of Tweets', min_value = 0, max_value = 180000)
