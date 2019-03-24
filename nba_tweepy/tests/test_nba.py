from unittest import TestCase
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime as dt

import nba_tweepy as nt
import credentials as creds


class TestNba(TestCase):
    def setUp(self):
        self.nba = nt.NBA(creds.consumer_key, creds.consumer_secret, creds.access_key, creds.access_secret)

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

    def test_get_all_player_tweets_returns_df(self):
        test_df = self.nba.get_player_tweets( self.nba.players.SCREEN_NAME[0])
        self.assertTrue(len(test_df.index) > 0)

    def test_get_all_player_tweets_min_no_max(self):
        test_df = self.nba.get_player_tweets( self.nba.players.SCREEN_NAME[0], min_date = '03-01-2019')
        self.assertEqual(test_df.TWEET_CREATE_DATE.min() , dt.datetime.strptime('03-01-2019', '%m-%d-%Y').date() )

    def test_get_all_player_tweets_max_no_min(self):
        test_df = self.nba.get_player_tweets( self.nba.players.SCREEN_NAME[0], max_date ='03-01-2019')
        self.assertEqual(test_df.TWEET_CREATE_DATE.max() , dt.datetime.strptime('03-01-2019', '%m-%d-%Y').date() )

    def test_get_all_player_tweets_date_range(self):
        test_df = self.nba.get_player_tweets( self.nba.players.SCREEN_NAME[0], min_date = '03-01-2019',max_date = '03-18-2019')
        self.assertEqual(test_df.TWEET_CREATE_DATE.min() , dt.datetime.strptime('03-01-2019', '%m-%d-%Y').date() )
        self.assertEqual(test_df.TWEET_CREATE_DATE.max() , dt.datetime.strptime('03-18-2019', '%m-%d-%Y').date() )

    def test_get_all_player_tweets_single_date(self):
        test_df = self.nba.get_player_tweets( self.nba.players.SCREEN_NAME[0], min_date = '03-01-2019',max_date = '03-01-2019')
        self.assertEqual(test_df.TWEET_CREATE_DATE.min() , dt.datetime.strptime('03-01-2019', '%m-%d-%Y').date() )
        self.assertEqual(test_df.TWEET_CREATE_DATE.max() , dt.datetime.strptime('03-01-2019', '%m-%d-%Y').date() )
    

