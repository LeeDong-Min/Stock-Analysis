from datetime import datetime
import backtrader as bt


class MyStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()

            else:
                if self.rsi > 70:
                    self.order = self.sell()


cerebro = bt.Cerebro()
cerebro.addstrategy(MyStrategy)
data = bt.feeds.YahooFinanceData(dataname="005930.KS", fromdate=datetime(2019, 1, 1), todate=datetime(2020, 12, 31))
cerebro.adddata(data)
cerebro.broker.setcash(10000000)
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

print(f"Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW")
cerebro.run()
print(f"Final Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW")
cerebro.plot()
