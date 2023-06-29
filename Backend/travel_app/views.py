from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import tweepy

def get_twitter_api():
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def get_tweets(request):
    # Get the location from the request
    location = request.GET.get('location')

    # Get the Twitter API instance
    api = get_twitter_api()

    try:
        # Fetch tweets from the specified location
        tweets = api.search(q=location, count=10)

        # Process the tweets as needed

        # Return the JSON response
        return JsonResponse({'tweets': tweets})
    except tweepy.TweepError as e:
        # Handle any errors that occur during the API request
        return JsonResponse({'error': str(e)})


# Create your views here.
