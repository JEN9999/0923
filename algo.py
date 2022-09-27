#크립토 트레이딩 알고리즘
#pandas matplotlib(그래프 유용) 설치

from coin_bot import CoinBot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bot = CoinBot()
client = bot.client

#가격을 보고있다가 어떤 코인이 X가격이 되면 산다
def buy_coin_at_price(client, symbol, target_price):
  ticker_info = client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice']
  last_price = round(float(last_price),2)
  if last_price <= target_price:
    return client.order_market_buy(
      symbol = symbol,
    quantity = 1.0,
    )

  return None

#어떤코인이 Y가격이 되면 판다.
def sell_coint_at_price(client,symbol, target_price):
  ticker_info = client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice']
  last_price = round(float(last_price),2)
  if last_price >= target_price:
    return client.order_market_sell(
      symbol = symbol,
    quantity = 1.0,
    price = str(target_price)
    )
#이동평균선 지금까지의가격이필요.
#1. 이동평균선 (moving average) 보다 낮으면사고
#2. 이동편균선보다 가격이 높으면 팔아라
def get_price_history(client):
  klines = client.get_historical_klines('BTCUSDT', '1h','2 week ago UTC')
  for line in klines:
    del line[5:]

  df = pd.DataFrame(klines, columns= ['date','open','high','low','close'])
  df.set_index('date', inplace=True)
  df.index = pd.to_datetime(df.index, unit="ms")
  
  return df.astype(float)

def trade_based_on_5_sma(client):
  df = get_price_history(client)
  #이동평균선 구하기  끝난가격을가지고
  #column 추가 >>이동평균선  pandas
  df['5_sma'] = df['close'].rolling(5).mean()
  df['buy'] = np.where(df['5_sma'] > df['close'], 1, 0)#column 추가
  df['sell'] = np.where(df['5_sma'] <= df['close'], 1, 0)#column 추가

  return df

def trade_based_on_crossover(client):
  df = get_price_history(client)
  df['5_sma'] = df['close'].rolling(5).mean()
  df['15_sma'] = df['close'].rolling(15).mean()

  df['signal'] = np.where(df['5_sma'] > df['15_sma'],1,0)
  #pandas
  df['position'] = df['signal'].diff()

  #단기이평선이 장기이평선을 위에서 밑으로 교차
  df['buy_cross'] = np.where(df['position'] == 1, df['5_sma'], np.NaN)
  #단기이평선이 장기이평선을 밑에서 위로 교차
  df['sell_cross'] = np.where(df['position'] == -1, df['5_sma'], np.NaN)
  
  return df

def plot_crossover_graph(client):
  df = trade_based_on_crossover(client)
  df[['5_sma','15_sma']].plot()
  #교차시점
  plt.scatter(df.index, df['buy_cross'], color="blue", label="Buy", marker= "^", alpha=1)
  plt.scatter(df.index, df['sell_cross'], color="red", label="Sell", marker= "v", alpha=1)
  
  plt.xlabel("Date")
  plt.ylabel("Price")#moving average
  plt.show()
  
# buy_coin_at_price(client, 'BTCUSDT', 100)
# print(get_price_history(client))
# print(trade_based_on_5_sma(client))

plot_crossover_graph(client)
