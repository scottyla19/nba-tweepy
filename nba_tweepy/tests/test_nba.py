from unittest import TestCase
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime as dt

import nba_tweepy as nt
import credentials as creds
import pandas as pd
import warnings

class TestNba(TestCase):
    def setUp(self):
        self.nba = nt.NBA(creds.consumer_key, creds.consumer_secret, creds.access_key, creds.access_secret)
        warnings.simplefilter('ignore', category=ResourceWarning)

    def test_is_auth(self):
        self.assertEqual(self.nba.api.me().screen_name, creds.myScreenName)

    # takes too long
    # def test_update_player_list(self):
    #     # player_csv_modified_date = os.path.getmtime(os.path.join(os.path.dirname(os.path.dirname(__file__),'data/player-list.csv')))
    #     nba.update_player_list()
    #     player_list_mod_date = dt.datetime.fromtimestamp(os.path.getmtime(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data/player-list.csv')))
    #     today = dt.datetime.now()
    #     self.assertTrue((today-player_list_mod_date).total_seconds() < 1)
        
    # def test_get_player_handle(self):
    #     pass

    # def test_get_all_player_tweets_returns_df(self):
    #     test_df = self.nba.get_all_tweets( self.nba.players.SCREEN_NAME[0])
    #     self.assertTrue(len(test_df.index) > 0)

    # def test_get_all_player_tweets_min_no_max(self):
       
    #     test_df = self.nba.get_all_tweets( self.nba.players.SCREEN_NAME[0], min_date =  '03-01-2019')
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.min() , pd.Timestamp(dt.datetime.strptime('03-01-2019', "%m-%d-%Y").date()) )

    # def test_get_all_player_tweets_max_no_min(self):
    #     test_df = self.nba.get_all_tweets( self.nba.players.SCREEN_NAME[0], max_date ='03-01-2019')
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.max() , pd.Timestamp(dt.datetime.strptime('03-01-2019', "%m-%d-%Y").date()))

    # def test_get_all_player_tweets_date_range(self):
    #     test_df = self.nba.get_all_tweets( self.nba.players.SCREEN_NAME[0], min_date = '03-01-2019',max_date = '03-18-2019')
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.min() , pd.Timestamp(dt.datetime.strptime('03-01-2019', "%m-%d-%Y").date()) )
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.max() , pd.Timestamp(dt.datetime.strptime('03-18-2019', "%m-%d-%Y").date()))

    # def test_get_all_player_tweets_single_date(self):
    #     test_df = self.nba.get_all_tweets( self.nba.players.SCREEN_NAME[0], min_date = '03-01-2019',max_date = '03-01-2019')
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.min() , pd.Timestamp(dt.datetime.strptime('03-01-2019', "%m-%d-%Y").date())) 
    #     self.assertEqual(test_df.TWEET_CREATE_DATE.max() , pd.Timestamp(dt.datetime.strptime('03-01-2019', "%m-%d-%Y").date()))
    
    # def test_get_team_tweets_no_players(self):
    #     team_tweets = self.nba.get_team_tweets('spurs', include_players = False)
    #     self.assertTrue(team_tweets.SCREEN_NAME.nunique() == 1)
    #     self.assertTrue(team_tweets.SCREEN_NAME[0]== 'spurs')

    # def test_get_team_tweets_include_players(self):
    #     team_tweets = self.nba.get_team_tweets('Mavericks', include_players = True)
    #     df = pd.merge(team_tweets, self.nba.players, on= 'SCREEN_NAME')
    #     self.assertTrue(team_tweets.SCREEN_NAME.nunique() > 1)
    #     self.assertTrue(df.TEAM_NAME.nunique() == 1)
    #     self.assertTrue(df.TEAM_NAME[0] == 'Mavericks')

    def test_get_player_handle(self):
        handle = self.nba.get_player_handle('LeBron James')
        self.assertEqual(handle, 'KingJames')

    def test_get_player_handle_not_NBA(self):
        handle = self.nba.get_player_handle('Scott LaForest')
        self.assertEqual(handle, 'Unfortunately, {} is not in the NBA.'.format('Scott LaForest'))

    def test_get_player_handle_single_name(self):
        handle = self.nba.get_player_handle('Nene')
        self.assertEqual(handle, 'NeNeLeakes')

    def test_get_player_handle_suffix(self):
        handle = self.nba.get_player_handle('Marvin Bagley III')
        self.assertEqual(handle, 'MB3FIVE')

  
       
    def test_get_bombs_woj(self):
        bombs = self.nba.get_woj_bombs()
        filtered = bombs[(bombs.SCREEN_NAME.str.contains('wojespn') == True)]
        self.assertEqual(len(filtered.index) , len(bombs.index))
       
    def test_get_bombs_shams(self):
        bombs = self.nba.get_shams_scoops()
        filtered = bombs[(bombs.SCREEN_NAME.str.contains('ShamsCharania') == True)]
        self.assertEqual(len(filtered.index) , len(bombs.index))

       

