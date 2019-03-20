from  nba_twitter import NBA
import credentials as creds
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)




nba = NBA(creds.consumer_key, creds.consumer_secret, creds.access_key, creds.access_secret)
print(NBA.update_player_list())
print(nba.api.me().screen_name)