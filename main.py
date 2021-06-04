import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.golden_cross import GoldenCross

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_price = pd.read_csv("data_set/spy.csv", index_col='Date', parse_dates=True)


feed = bt.feeds.PandasData(dataname = spy_price)
cerebro.adddata(feed)


cerebro.addstrategy(GoldenCross)

cerebro.run()
cerebro.plot()
