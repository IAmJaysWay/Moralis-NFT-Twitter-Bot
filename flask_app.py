
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, abort
import tweepy


app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        CONSUMER_KEY = "<API Key>"
        CONSUMER_SECRET = "<API Secret>"
        ACCESS_KEY = "<Access Keyt>"
        ACCESS_SECRET = "<Access Secret>"

        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        tweet = 'CryptoPunk #{name} just sold for Ξ{price}'.format(name= request.get_json()['name'], price = request.get_json()['price'])


        f_write = open('tweetMedia.png', 'wb')
        f_write.write(bytes(request.get_json()['content']['data']))
        f_write.close()

        postMedia = api.media_upload("tweetMedia.png")

        mediaID = postMedia.media_id_string

        api.update_status(status=tweet, media_ids = [mediaID])
    else:
        abort(400)

