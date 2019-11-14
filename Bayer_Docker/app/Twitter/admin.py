#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:       
#   
#   Description:
#
#


from django.contrib import admin
from .models import SearchTerm, Location, StopWord

# Register your models here.

admin.site.register(SearchTerm)
admin.site.register(StopWord)
admin.site.register(Location)
