import numpy as np 
import pandas as pd 
import os 
from sys import argv
import time 
from datetime import datetime
from time import mktime 
import feedparser 


class WatchFiveThirtyEight():

    def watch_rss(self, rss_feed):
        """
        TODO docs
        """
        try:
            # get current time
            now = datetime.now()
            
            # parse data source
            newsfeed = feedparser.parse(rss_feed)

            # get all articles
            articles = newsfeed.entries

            for article in articles:
                # get published times
                raw_time = article['published_parsed']

                # convert to datetime object
                format_time = datetime.fromtimestamp(mktime(raw_time))


        except Exception as e: 
            print("an error occured: {}".format(e))
            return None 



    # TODO create db function
    def create_database(self):
        pass




                                


    #self.create_sample_data()


if __name__ == '__main__':

    # start the app
    app = WatchFiveThirtyEight()

    # print some output messages
    rss_fname = argv[1]

    print("starting app")
    app.watch_rss(argv[1])