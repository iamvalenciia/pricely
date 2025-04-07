import json
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    try:
        consumer_key = os.environ['CONSUMER_KEY'] or os.getenv('CONSUMER_KEY')
        consumer_secret = os.environ['CONSUMER_SECRET'] or os.getenv('CONSUMER_SECRET')
        access_token = os.environ['ACCESS_TOKEN'] or os.getenv('ACCESS_TOKEN')
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET'] or os.getenv('ACCESS_TOKEN_SECRET')
        
        # Initialize Twitter client
        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        
        # Create Tweet
        # Extract tweet text from event if provided, otherwise use default
        tweet_text = event.get('tweet_text', "This Tweet was Tweeted from AWS Lambda!")
        
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data['id']
        tweet_url = f"https://twitter.com/user/status/{tweet_id}"
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Tweet successfully posted',
                'tweet_id': tweet_id,
                'tweet_url': tweet_url
            })
        }
    
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error posting tweet',
                'error': str(e)
            })
        }