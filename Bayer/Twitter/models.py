


from django.db import models

# Create your models here.


class Tweet(models.Model):
    full_text = models.CharField(max_length=400) # full text of tweet
    user_id = models.CharField(max_length=60)
    tweet_id = models.CharField(unique = True, max_length=100)
    sentiment = models.DecimalField(max_digits=3, decimal_places=2)
    #
    #   Commented fields have not been implemented yet but will be in the future
    #   need to go through twitter return and find some values and others need to be sure of how
    #
    #date = models.DateField(auto_now=False, auto_now_add=False)
    #likes = models.PositiveIntegerField()
    #retweets = models.PositiveIntegerField()
    #hashtags = models.CharField(max_length=50)
    #location  = models.CharField(max_length=50)
    
    def __str__(self):
        tweet = self.user_id + '</br>' + self.tweet_id + '</br></br>'
        return tweet
    
        
        
class WordList(models.Model):
    word = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    tweet_id = models.ForeignKey(Tweet, on_delete=models.PROTECT)  
    
    def __str__(self):
        word = self.word + ': ' + self.count
        return word
    
class Hashtags(models.Model):
    # hashtags can seemingly be of length of the tweet making the whole tweet the hashtag,
    # so they need to big enough to hold that.  
    hashtag = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    tweet_id = models.ForeignKey(Tweet, on_delete=models.PROTECT)
    
    def __str__(self):
        hastag = self.hastag + ': ' + self.count
        return hastag
    
