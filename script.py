import numpy as np 
import pandas as pd 
import os 
from sys import argv
import time 
from datetime import datetime
import feedparser 


class WatchFiveThirtyEight():

    def watch_rss(self, rss_feed):
        """
        TODO docs
        """
        try:
            # data source
            newsfeed = feedparser.parse(rss_feed)

            # get first 15 entries
            entries = newsfeed.entries[1:100]

            for entry in entries:
                print('entry: {}'.format(entry))

            pass

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

    # get the current time
    current_time = datetime.now()

    # print some output messages
    rss_fname = argv[1]

    print("starting app")
    app.watch_rss(argv[1])