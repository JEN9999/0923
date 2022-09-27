from binance.client import Client


class CoinBot:
    #ToDO : API KEY 코드에서 없애기
    API_KEY = 'CpTUySnXt57UtWj5wOedmThtXtMZP8FDojxbEgk9d1Iz4mojF3l1VFGuOmeXXB0p'
    API_SECRET = 'cplg01rHhXT8CQCw6yn4w0x9T2ApxN9cPpYlwUSQtJLpUoBDx9g2O68yMyjYVmNL'

    def __init__(self):
        self.client = Client(self.API_KEY, self.API_SECRET, testnet=True)

    def get_account(self):
        return self.client.get_account()

    def buy_coin_at_discount(self, symbol, quantity):
        #1.코인의 지금가격을 불러온다
        ticker_info = self.client.get_ticker(symbol=symbol)
        last_price = ticker_info['lastPrice']
        #2. 코인의 지금가격에서 10% 디스카운트된 가격계산
        discount_price = round((float(last_price)) * 0.9,
                               2)  # 1불일경우에 0불에 주문을 넣는 경우가 생김 >>
        #3. 그가격에 주문을 넣는다.
        return self.client.order_limit_buy(symbol=symbol,
                                           quantity=quantity,
                                           price=str(discount_price))

        print(last_price)
        print(discount_price)
        print(order)

    def sell_coin_at_premium(self, symbol, quantity):
        #1.코인의 지금가격을 불러온다
        ticker_info = self.client.get_ticker(symbol=symbol)
        last_price = ticker_info['lastPrice']
        #2. 코인의 지금가격에서 10% 프리미엄 된 가격계산
        premium_price = round((float(last_price)) * 1.1,
                              2)  # 1불일경우에 0불에 주문을 넣는 경우가 생김 >>
        #3. 그가격에 주문을 넣는다.
        return self.client.order_limit_sell(symbol=symbol,
                                            quantity=quantity,
                                            price=str(premium_price))

    def cancel_all_open_orders(self):
        open_orders = self.client.get_open_orders()
        for order in open_orders:
            result = self.client.cancel_order(symbol=order['symbol'],
                                              orderId=order['orderId'])

    def sell_coin_at_market_price(self, symbol, quantity):
        order = self.client.order_market_sell(symbol=symbol, quantity=quantity)
        return order


bot = CoinBot()
# bot.buy_coin_at_discount('LTCUSDT',1)
# order_result = bot.buy_coin_at_market_price('LTCUSDT', 1)
# print(order_result)
# bot.cancel_all_open_orders()
# print(bot.client.get_open_orders())
# print(bot.get_account())
# print(bot.sell_coin_at_market_price('BNBUSDT',1))
