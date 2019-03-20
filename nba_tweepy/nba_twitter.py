import tweepy
import pandas as pd
import requests

class NBA:
   def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
      self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      self.auth.set_access_token(access_token, access_token_secret)
      self.api = tweepy.API(self.auth)
      self.players = pd.read_csv('data/player-list.csv')


   @property
   def get_player_tweets(self, player):
      all_tweets = []

      #make initial request for most recent tweets (200 is the maximum allowed count)
      new_tweets = self.api.user_timeline(screen_name = player,count=200)

      #save most recent tweets
      all_tweets.extend(new_tweets)

      #save the id of the oldest tweet less one
      oldest = all_tweets[-1].id - 1

      #keep grabbing tweets until there are no tweets left to grab
      while len(new_tweets) > 0:
   #         print ("getting tweets before {}".format(oldest))

         #all subsiquent requests use the max_id param to prevent duplicates
         new_tweets = self.api.user_timeline(screen_name = player,count=200,max_id=oldest)

         #save most recent tweets
         all_tweets.extend(new_tweets)

         #update the id of the oldest tweet less one
         oldest = all_tweets[-1].id - 1
         
   #         print ("...{} tweets downloaded so far".format(len(all_tweets)))
      #transform the tweepy tweets into a 2D array that will populate the csv	
      outtweets = [[player, tweet.id_str, tweet.created_at, 
                     tweet.text, tweet.created_at.date(), tweet.created_at.time()] for tweet in all_tweets]
   #     #write the csv	
   #     with open('%s_tweets.csv' % screen_name, 'wb') as f:
   #         writer = csv.writer(f)
   #         writer.writerow(["id","created_at","text"])
   #         writer.writerows(outtweets)
      df = pd.DataFrame(data=outtweets, columns=['SCREEN_NAME','TWEET_ID','TWEET_CREATE_TIMESTAMP',
                                                'TWEET_TEXT', 'TWEET_CREATE_DATE', 'TWEET_CREATE_TIME'])
      
      return df

   @staticmethod
   def update_player_list (season='2018-19'):
      # url = 'https://stats.nba.com/stats/commonallplayers/?LeagueID=00&Season={}&IsOnlyCurrentSeason=1'.format(season)
      # headers = {'host': 'stats.nba.com',
      #          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
      #          'cache-control': 'no-cache',
      #          'pragma': 'no-cache',
      #          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      #             'accept-encoding': 'gzip, deflate',
      #          'accept-language': 'en-US,en;q=0.9',
      #          'connection': 'keep-alive',
      #          'upgrade-insecure-requests': '1'}

      # r = requests.get(url,  headers=headers)
      # jsn = r.json()

      # rjson = jsn['resultSets'][0]
      # headers= rjson['headers']
      # rowSet = rjson['rowSet']
      # rows = rowSet[1:]

      # players = pd.DataFrame(rows, columns=headers)
      # # players.dropna(axis=0,how='all',inplace=True)
      # players['SCREEN_NAME'] = players.DISPLAY_FIRST_LAST.apply(_get_player_handle )
      # players.to_csv('data/player-list.csv')
      
      return 'Updating player list...'
    #use code from notebook that his stats.nba.com endpoint for players
    #overwrite and update current csv

   def _get_player_handle(self, name):
      resp = ''
      try:
         resp = self.api.search_users(name)[0]
      except:
         print(name)
         return ''
      return resp.screen_name
