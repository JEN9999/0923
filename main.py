# 일론 머스크 트윗할때 코인사기
# 트위터 API 필요

#1. 일론머스크의 트윗을 검색
#userID
#https://api.twitter.com/2/users/by?usernames=twitterdev,twitterapi,adsapi&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at


#https://api.twitter.com/2/users/:id/timelines/reverse_chronological?tweet.fields=created_at&expansions=author_id&user.fields=created_at&max_results=5

#2. 트윗에서 코인 이름 검색
#3. 코인이름이 검색되면 그 코인 사기
import requests
from coin_bot import CoinBot


class TwitterClient:
  def __init__(self):
    bearer_token = "bearer_token = 'AAAAAAAAAAAAAAAAAAAAAG%2F5hQEAAAAAk6MS7%2ByA%2FiykrdJGmZvgfjOUjvw%3D3AOcPNEs6IMsz1tLFBfn92JUeE0OO5Ce9GSx0S05oZr518odDZ'
    self.headers = {'Authorization':f'Bearer {bearer_token}'}

  def get_user(username):
    url = f'https://api.twitter.com/2/users/by/username/{username}'
    raw_resp = requests.get(url, headers=self.headers)
      
  
    return raw_resp.json()
    


  def get_tweets_by_user_id(self,user_id):
   
    url = f'https://api.twitter.com/2/users/{user_id}/tweets'
    raw_resp = requests.get(url, 
      headers=self.headers,
      params={
        'max_results':100,
      })
                           
    resp = raw_resp.json()
    print(resp)


def is_bitcoin_in_tweet(self,tweet_info):
  text = tweet_info['text']
  return "bitcoin" in text.lower():
    

def buy_bitcoin_if_elon_says_so():
  twitterClient = TwitterClient()
  bot = CoinBot()
  tweets_by_elon = get_tweets_by_user_id(44196397)
  for tweet in tweets_by_elon:
    is_bitcoin_included = is_bitcoin_in_tweet(tweet)
    if(is_bitcoin_included):
      #buy bitcoin
      bot.buy_coin_at_discount('BTCUSDT',1)
      print("주문 완료!",order)
      
  
  
# get_user('elonmusk')

# tweets_by_elon = get_tweets_by_user_id(44196397)
# print(tweets_by_elon) 

# tweet_info = {'id':'123125215','text':'Bitcoin'}
# is_bitcoin_in_tweet = find_coin_from_tweet(tweet_info)
# print(is_bitcoin_in_tweet)

