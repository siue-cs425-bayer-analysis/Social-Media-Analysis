from django.urls import path

from . import views
from Reddit.views import requestSearch

urlpatterns = [
	path('', views.index, name='index'),
	path('redditsearch', requestSearch, name='redditsearch'),
]
