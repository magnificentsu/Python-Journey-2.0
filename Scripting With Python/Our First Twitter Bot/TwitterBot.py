import tweepy

auth = tweepy.OAuthHandler('rI7Oc7tW94YM1HRwiHomGH5U4', 'ypRdHkmb17zAbkybIdvjEGYbgW0Bp5Nhtg7LrcKITYF0TTJOaq')
auth.set_access_token('1743920980546998272-9JVAqBmLz4wVMPBGpPjsPQ3S5OThxI', 'jaSezK4x9HXcGiB8imbZSbwphTiIRKFUAdjK8yvsYN1WT')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.get_followers
print(user)