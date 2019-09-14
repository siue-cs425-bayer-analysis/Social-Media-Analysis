#   Carl Grissom
#   sentiment.py   
#   3/27/2019
#   Description: functions for sentiment analysis
#
#
#



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_score(sentence):
    score = analyzer.polarity_scores(sentence)
    return score
