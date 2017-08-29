import tweepy, time, sys
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
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
