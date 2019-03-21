from unittest import TestCase
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import nba_tweepy as nt
import credentials as creds



class TestNba(TestCase):
    def test_is_auth(self):
        nba = nt.NBA(creds.consumer_key, creds.consumer_secret, creds.access_key, creds.access_secret)
        self.assertEqual(nba.api.me().screen_name, creds.myScreenName)
