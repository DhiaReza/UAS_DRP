import tweepy
#from . import Keys

'''
key dibawah isi punya snediri atau minta fahreza
'''

consumer_key = "bkZI6iYjM0gxoLMqLosaddsadkuyrGMO"
consumer_secret = "InO2v0Wl52j00qqXaCP6elapfTQhz1Zcy5y0tk4GqwewqecAhaoyIdEr"
access_token = "1459732225948151818-0zjGJuiLA3FgGkB2FE7HcuusadUz5pNHL"
access_token_secret = "gehkg4ZW9C3pBVayzmSvCb1Brm80sqpbZvyesadjYeX8Eg9G"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "argentina vs france"
# Language code (follows ISO 639-1 standards)
language = "en"

start_time="2022-11-01T14:55:00Z"
end_time="2022-11-10T01:49:00Z"
output=open("tweets.txt", "a" , encoding="UTF-8")

# Calling the user_timeline function with our parameters
results = api.search_tweets(q=query, lang=language, result_type="mixed", count="5000")

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.text)
   output.write(str(tweet.text))
   output.write("\n")