import sys

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
from twython import TwythonStreamer, Twython

from keys import *

class BappleStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'id' in data:
            if 'text' in data:
                print 'attempting to retweet:', data['text'].encode('utf-8')
            twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            try:
                response = twitter.retweet(id=data['id'])
                if 'created_at' in response:
                    print 'rt succeeded at', response['created_at']
            except Exception, err:
                print "*** could not rt because", err, "skipping"
        else:
            print '**** tweet has no id skipping'

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

def main(argv=sys.argv):
    stream = BappleStreamer(APP_KEY, APP_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=['applemusic wtf', 'apple music wtf', 'applemusic offended', 'apple music offended'])
if __name__ == '__main__':
    main()