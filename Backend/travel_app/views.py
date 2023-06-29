from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import http.client
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_tweets():
    conn = http.client.HTTPSConnection("twitter154.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "5c5c542266mshe01e9f5df0e7b6bp1ade18jsn9ee7c45949eb",
        'X-RapidAPI-Host': "twitter154.p.rapidapi.com"
    }
    conn.request("GET", "/search/search?query=newyork&section=top&min_retweets=1&min_likes=1&limit=5&start_date=2022-01-01&language=en", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    
    # Parse the JSON data
    parsed_data = json.loads(data)
    print(parsed_data)  # Print the parsed data for debugging
    tweets = parsed_data['results']
    
    # Return JSON response
    return JsonResponse({'tweets': tweets})


#take the json and make a list of the tweets only

def get_text_from_tweets(json_file):
    lst = []
    for i in json_file['tweets']:
        lst.append(i['text'])
    return lst


def analyze_sentiment(tweet_texts):
    # Initialize the SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()

    # Calculate aggregate sentiment score
    aggregate_score = 0
    for text in tweet_texts:
        sentiment_scores = sid.polarity_scores(text)
        aggregate_score += sentiment_scores['compound']

    # Normalize the aggregate score
    num_tweets = len(tweet_texts)
    normalized_score = aggregate_score / num_tweets

    return normalized_score

def tweets_view(request):
    json_file = get_tweets()
    tweet_texts = get_text_from_tweets(json_file)
    aggregate_score = analyze_sentiment(tweet_texts)

    context = {
        'aggregate_score': aggregate_score
    }

    return JsonResponse(context)