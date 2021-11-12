# Cloned from https://github.com/julioadl/ds101/blob/master/twitter_workshop/twitter.py

import oauth2 as oauth
import urllib.request as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = ""
api_secret = ""
access_token_key = ""
access_token_secret = ""

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/filter.json?track=trump"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  data={'tweets':[]}
  maximum = 5
  i = 0

  for line in response:
    print(line.strip())
    if i == maximum:
      break
    else:
      data['tweets'].append(line.strip())
    i += 1

  #json.dump(data, open('test.json', 'w'))


if __name__ == '__main__':
  fetchsamples()
