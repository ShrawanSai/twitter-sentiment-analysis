#!/usr/bin/env python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
def readtweet():
    #consumer key, consumer secret, access token, access secret.
    ckey="WNxuoNZkT2YfX65mio3eAvf8f"
    csecret="QxhuS1xu6NxyfhiSErxTmhYgRgK8HupSPJzVhBWkSXIJEZ4hme"
    atoken="1071084889154310145-qYXNlTJtyne6iqaaaRDipyYWMR7wyh"
    asecret="zjrmqthh0W7cYuVGjt7Uztgn6tgkzWZCUEhUob8m6CxKd"

    import newsread
    import os
    x1=os.getpid()
    f=open('pid.txt','w')
    f.write(str(x1))
    f.close()
    ####
    class listener(StreamListener):
        def __init__(self, time_limit=60):
            self.start_time = time.time()
            self.limit = time_limit

        def on_data(self, data):
            try:
                          
                if (time.time() - self.start_time) < self.limit:
                    filed=open('livestream1.txt','a')
                    tweet1= data.split(',"text":"')[1].split('","source":"')
                    tweet=tweet1
                    
                    if len(tweet[0])>1000:
                        pass
                    else:
                        print(tweet[0])
                        print(len(tweet[0]))
                        print('----------------')
                        filed.write(tweet[0])
                        filed.write('\n')
                        filed.close()
                    
                    return(True)
                else:
                    return False
            except BaseException as e:
                #print('Error: ')
                #print(str(e))
                time.sleep(5)

        def on_error(self, status):
            #print(status)
            pass

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)




            
    x=newsread.returncleaned()
    #print(x)
    f=open('keywords.txt','w')
    for i in x:
        f.write(i)
        f.write('\n')
    f.close()
    twitterStream = Stream(auth, listener=listener(time_limit=10))
    twitterStream.filter(track=x,languages=["en"])
