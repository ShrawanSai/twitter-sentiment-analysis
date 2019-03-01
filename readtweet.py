import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
ckey="WNxuoNZkT2YfX65mio3eAvf8f"
csecret="QxhuS1xu6NxyfhiSErxTmhYgRgK8HupSPJzVhBWkSXIJEZ4hme"
atoken="1071084889154310145-qYXNlTJtyne6iqaaaRDipyYWMR7wyh"
asecret="zjrmqthh0W7cYuVGjt7Uztgn6tgkzWZCUEhUob8m6CxKd"

import newsread

####
class listener(StreamListener):

    def on_data(self, data):
        try:
            
            
            filed=open('livestream1.txt','a')
            tweet1= data.split(',"text":"')[1].split('","source":"')
            tweet=tweet1
            print(tweet[0])
            print(len(tweet[0]))
            print('----------------')
            if len(tweet[0])>1000:
                pass
            else:
                filed.write(tweet[0])
                filed.write('\n')
                filed.close()
            
            return(True)
        except BaseException as e:
            print('Error: ')
            print(str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)




	
x=newsread.returncleaned()
print(x)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=x,languages=["en"])
    
    
    
    