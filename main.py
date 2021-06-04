import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.golden_cross import GoldenCross
from strategies.buy_hold import BuyHold

strategies = {
    "golden_cross" : GoldenCross,
    "buy_hold" : BuyHold
}


parser = argparse.ArgumentParser()
parser.add_argument("strategy", help = "which strategy to run", type = str)
args = parser.parse_args();

if not args.strategy in strategies:
    print("invalid startegy, must be in {}".format(strategies.keys()))
    sys.exit()



cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_price = pd.read_csv("data_set/spy.csv", index_col='Date', parse_dates=True)


feed = bt.feeds.PandasData(dataname = spy_price)
cerebro.adddata(feed)


cerebro.addstrategy(strategy=strategies[args.strategy])

cerebro.run()
cerebro.plot()
