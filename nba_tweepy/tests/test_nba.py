from unittest import TestCase
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime as dt

import nba_tweepy as nt
import credentials as creds
nba = nt.NBA(creds.consumer_key, creds.consumer_secret, creds.access_key, creds.access_secret)


class TestNba(TestCase):
    def test_is_auth(self):
        
        self.assertEqual(nba.api.me().screen_name, creds.myScreenName)

    def test_update_player_list(self):
        # player_csv_modified_date = os.path.getmtime(os.path.join(os.path.dirname(os.path.dirname(__file__),'data/player-list.csv')))
        nt.NBA.update_player_list()
        player_list_mod_date = dt.date.fromtimestamp(os.path.getmtime('data/player-list.csv'))
        today = dt.datetime.today()
        self.assertEqual(player_list_mod_date, today)
        pass
