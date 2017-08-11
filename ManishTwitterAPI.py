#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'J7xgpFgQPLivptDyfbRsZsG8i'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'vxcDHEPJ5PR5ipPgxYWQ0YejOZHfZj0HDG4cbRwXGynB6XrmyB'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '350069347-c2PU7pmLnIIPQ3JZDDjYw0vCqFOqprWuAi28uXpF'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'L6SnCuwKIEV2l0lUpzx5xhqqp2y0lB20ZRJitOJZ1U9JH'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
# filename=open(argfile,'r')
# f=filename.readlines()
# filename.close()
 
# for line in f:
#     api.update_status(line)
#     time.sleep(900)#Tweet every 15 minutes
print '\nFollowers in Twitter\n'
for user in tweepy.Cursor(api.followers, screen_name="ManishShaw1").items():
    print user.screen_name

print '\nFollowing in Twitter\n'
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    print friend.screen_name
