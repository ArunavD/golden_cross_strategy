<!--Head-->
# golden_cross_strategy

![Golden_cross strategy](https://img.shields.io/badge/strategy-golden__cross-blue)
![S&P500](https://img.shields.io/badge/S%26P-500-brightgreen)
![nifty_50](https://img.shields.io/badge/NIFTY-50-orange)


![logo](https://github.com/ArunavD/golden_cross_strategy/blob/master/Figure_0.png)

I have tested golden cross strategy in S&P500 (SPY) and NIFTY_50 using python and backtrader. Also added buy and hold strategy to get the idea of calling strategies from console.



## Contents

* [What is moving average?](#What-is-moving-average)
* [What is Golden Cross strategy?](#What-is-Golden-Cross-strategy)
* [Libraries](#Libraries)
* [Description of each file](#Description-of-each-file)
* [Datasets](#Datasets)
* [How to use?](#How-to-use)




## What is moving average?

A moving averageis a tool used by technical analysts to track the price movements of a security. It plots average prices over a defined period of time, with the moving average typically overlaid onto a candlestick or bar chart. The bars or candlesticks show the price data for each time period.



## What is Golden Cross strategy?

The golden cross occurs when a short-term moving average (here I have taken 50 days) crosses over a major long-term moving average (here I haven taken 200 days) to the upside and is interpreted by analysts and traders as signaling a definitive upward turn in a market.



<!-- Libraries -->
## Libraries

+ [backtrader](https://www.backtrader.com) - It is an open-source framework that allows for strategy testing on historical data.
+ [pandas](https://pypi.org/project/pandas/) - the most powerful and flexible open source data analysis / manipulation tool.
+ [math](https://pypi.org/project/python-math/) - It provides us access to some common math functions and constants in Python.
+ [os](https://www.geeksforgeeks.org/os-module-python-examples/) - The OS module in Python provides functions for interacting with the operating system.
+ [sys](https://docs.python.org/3/library/sys.html) - This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
+ [argparse](https://docs.python.org/3/howto/argparse.html) - This tutorial is intended to be a gentle introduction to argparse, the recommended command-line parsing module in the Python standard library.


<!-- Description -->
## Description of each file

1. [moving_average.py](https://github.com/ArunavD/golden_cross_strategy/blob/master/moving_average.py) - Just an example of calculating moving average.
2. [main.py](https://github.com/ArunavD/golden_cross_strategy/blob/master/main.py) - This is the main method of the project where strategy is being executed with the help of backtrader's cerebro method.
3. [golden_cross.py](https://github.com/ArunavD/golden_cross_strategy/blob/master/strategies/golden_cross.py) - Here I have created the golden cross strategy using 50 days as the short term moving average and 200 days as the long term moving average.
4. [buy_hold.py](https://github.com/ArunavD/golden_cross_strategy/blob/master/strategies/buy_hold.py) - A simple strategy, just buy a specific amount of stocks and hold it for a long period.



## Datasets

I have only used S&P500 and NIFTY50 dataset which I ahve added bellow. Other stocks historical data also can be downloaded from [yahoo finance](https://in.finance.yahoo.com/).

+ [SPY](https://github.com/ArunavD/golden_cross_strategy/blob/master/data_set/spy.csv)
+ [NIFTY50]()



## How to use?

Finally one can run the project by typing the name of the strategy wants to use:

1. Golden Cross
```
$ python main.py golden_cross
```
2.Buy and Hold
```
$ python main.py buy_hold
```




