from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import tweepy

def get_twitter_api():
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api



# Create your views here.
