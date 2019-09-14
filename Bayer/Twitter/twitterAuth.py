#   Carl Grissom
#   twitterAuth.py   
#   3/27/2019
#   Description: twiter authentication
#
#
#

import twitter


# set up twiiter api 
consumer_key='sIiSc7R5pdzKAh8l9rz5jS9ZH'
consumer_secret='8egwSRdsWYtJf8r7ClUDOdOiIEHIRbIdaPN83qox1o7GWNiAvg'
access_token_key='1098622893091639296-2iAlSMhztu9d9BpLLtLdtQlDuiiQVd'
access_token_secret='Qt7bP8Vy4x6MmC4aFMLqQh3JycmLv7IF7XDN34RKjlspV'

# authenticate twitter api
api = twitter.Api(consumer_key, 
                    consumer_secret, 
                    access_token_key, 
                    access_token_secret, 
                    tweet_mode='extended')                  
