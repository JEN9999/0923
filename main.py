from binance.client import Client


class CoinBot:
    API_KEY = 'CpTUySnXt57UtWj5wOedmThtXtMZP8FDojxbEgk9d1Iz4mojF3l1VFGuOmeXXB0p'
    API_SECRET = 'cplg01rHhXT8CQCw6yn4w0x9T2ApxN9cPpYlwUSQtJLpUoBDx9g2O68yMyjYVmNL'

    def __init__(self):
        self.client = Client(self.API_KEY, self.API_SECRET, testnet=True)

    # def get_account(self):
    #     return self.client.get_account()

    def buy_coin_at_discount(self):
        #1.코인의 지금가격을 불러온다
        #3. 그가격에 주문을 넣는다.
        ticker_info = self.client.get_ticker(symbol="BTCUSDT")
        last_price = ticker_info['lastPrice']
        #2. 코인의 지금가격에서 10% 디스카운트된 가격계산
        discount_price = float(last_price) * 0.9

        print(last_price)
        print(discount_price)


# bot = CoinBot()
# print(bot.get_account())

bot = CoinBot()
bot.buy_coin_at_discount()
