import tweepy, time, sys
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'J7xgpFgQPLivptDyfbRsZsG8i'
CONSUMER_SECRET = 'vxcDHEPJ5PR5ipPgxYWQ0YejOZHfZj0HDG4cbRwXGynB6XrmyB'
ACCESS_KEY = '350069347-c2PU7pmLnIIPQ3JZDDjYw0vCqFOqprWuAi28uXpF'
ACCESS_SECRET = 'L6SnCuwKIEV2l0lUpzx5xhqqp2y0lB20ZRJitOJZ1U9JH'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

## To print the followers in Twitter
print '\nFollowers in Twitter\n'
for user in tweepy.Cursor(api.followers, screen_name="ManishShaw1").items():
    print user.screen_name

## To print names of people whom I am following
print '\nFollowing in Twitter\n'
for friend in tweepy.Cursor(api.friends).items():
    print friend.screen_name

## To Like a post of BoltIOT
data = api.user_timeline('boltiot');
tweet = data[0]
tweet.favorite();

# To Like all post of BoltIOT
for tweet in tweepy.Cursor(api.search, q='#IOT').items():
    try:
        tweet.favorite()
        print('Favorited the tweet by @' + tweet.user.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
