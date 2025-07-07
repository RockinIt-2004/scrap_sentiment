from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def analyze_reviews(review_list):
    result = []
    for review in review_list:
        sentiment = analyze_sentiment(review)
        result.append({'text': review, 'sentiment': sentiment})
    return result
def count_sentiments(analyzed_reviews):
    counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }
    for review in analyzed_reviews:
        sentiment = review.get("sentiment")
        if sentiment in counts:
            counts[sentiment] += 1
    return counts