import json
import tweepy
import http.client
# Import our Twitter bot account info
from secrets import *

def post_joke(event, context):
    post_response = {
        "statusCode": 200
    }
    
    try :
        # Get a random dad joke
        connection = http.client.HTTPSConnection("icanhazdadjoke.com", timeout=2)
        headers = { "Accept": "application/json" }
        connection.request('GET', '/', None, headers)
        response = connection.getresponse()
        if (response.status != 200):
            return {
                "statusCode": response.status,
                "statusMessage": response.reason
            }
        content = response.read().decode('utf-8')
        parsed_content = json.loads(content)
        joke = parsed_content['joke']
        
        # Authenticate with our Twitter bot account
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        
        # Post the joke tweet
        api.update_status(joke)
    except Exception as e:
        post_response = {
            "statusCode": 500,
            "statusMessage": e.message
        }
    
    return post_response
