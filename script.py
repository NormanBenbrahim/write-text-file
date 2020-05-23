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

            # initiate arrays
            times = []
            urls = []
            titles = [] 
            for article in articles:
                # get published times
                raw_time = article['published']
                format_time = raw_time[:-6]

                # convert to datetime object
                #format_time = datetime.fromtimestamp(mktime(raw_time))
                times.append(format_time)

                # get url
                url = article['url']
                urls.append(url)

                # get title
                title = article['title']
                titles.append(title)

            # collect into a dataframe
            dataset = pd.DataFrame({"title": titles, "link": urls, })
            print(dataset)

                


        except Exception as e: 
            print("an error occured: {}".format(e))
            return None                              


if __name__ == '__main__':

    # start the app
    app = WatchFiveThirtyEight()

    # print some output messages
    rss_fname = argv[1]

    print("starting app")
    app.watch_rss(argv[1])