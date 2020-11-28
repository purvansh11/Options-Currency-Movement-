U.S. Election Analysis
=======================

.. .. image:: https://img.shields.io/travis/constverum/Quantdom.svg?style=flat-square
..     :target: https://travis-ci.org/constverum/Quantdom
.. .. image:: https://img.shields.io/pypi/wheel/quantdom.svg?style=flat-square
..     :target: https://pypi.python.org/pypi/quantdom/
.. .. image:: https://img.shields.io/pypi/pyversions/quantdom.svg?style=flat-square
..     :target: https://pypi.python.org/pypi/quantdom/
.. .. image:: https://img.shields.io/pypi/l/quantdom.svg?style=flat-square
..     :target: https://pypi.python.org/pypi/quantdom/

This is a simple and powerful
currency analysis utility written in python,
that strives to let you focus on digital options strategies,
FX market movement,
and analyzing change in currency pairs.
It has been created as a useful and flexible tool
to give the clients a better analysis of movement
during the U.S. Elections
and let them evaluate their trading ideas easier
with minimal effort.
It's designed for people who are already comfortable
with Options strategies 
and who want to analyse their own trading strategies.




Features
--------

.. image:: /assets/Dig_Options.png
    :alt: Digital Options--Trade worked or not plot 

.. image:: /assets/Perc_Change.png
    :alt: % Change plot

.. image:: /assets/User_Inputs.png
    :alt: Fetch Inputs from User

* Free, open-source and cross-platform currency analysis tool
* Flexible expiry period: A timespan of upto 3 months can be used to analyse the trade
* In-depth currency Analysis: % Change vs Days around Elections from 2000-2016
* Charting and reporting that help visualize past results
* Correct and Accurate Results with 6 digit precision

.. Requirements
.. ------------

.. * Python **3.6** or higher
.. * `PyQt5 <https://pypi.python.org/pypi/PyQt5>`_
.. * `PyQtGraph <http://www.pyqtgraph.org/>`_
.. * `NumPy <http://www.numpy.org/>`_
.. * See `pyproject.toml <https://github.com/constverum/Quantdom/blob/master/pyproject.toml#L43-L50>`_ for full details.


.. Installation
.. ------------

.. Using the binaries
.. ##################

.. You can download binary packages for your system (see the `Github Releases <https://github.com/constverum/Quantdom/releases>`_ page for available downloads):

.. * For `Windows  <https://github.com/constverum/Quantdom/releases/download/v0.1/quantdom_0.1.exe>`_
.. * For `MacOS  <https://github.com/constverum/Quantdom/releases/download/v0.1/quantdom_0.1.dmg>`_
.. * For `Linux  <https://github.com/constverum/Quantdom/releases/download/v0.1/quantdom_0.1.zip>`_

.. Running from source code
.. ########################

.. You can install last *stable release* from pypi:

.. .. code-block:: bash

..     $ pip install quantdom

.. And latest *development version* can be installed directly from GitHub:

.. .. code-block:: bash

..     $ pip install -U git+https://github.com/constverum/Quantdom.git

.. After that, to run the application just execute one command:

.. .. code-block:: bash

..     $ quantdom


Usage
-----

1. Open - https://uselectionanalysis.herokuapp.com/.
2. Choose USD as CCY1 which is the base currency for the analysis
3. Choose a currency (CCY2) for the Options plot and %Change-vs-Days Around Election plot.
4. Select the Option type among American and European.
5. Enter the Strike in percentage (Eg. 0.9).
6. Select the expiry period of the deal.
7. Submit the data. Once this is done, you can analyze the results and Trade options of the Digital Options Strategy.


Digital Options Explained
-------------------------
Options are financial derivatives, so they receive their value from an underlying asset or security. Traditional options give buyers the ability, though not the obligation, to transact in the underlying security at a predetermined price—called the strike price—by date of expiration—or the end date of the contract.

Real World Example of a Bullish Digital Option
##############################################
Let's say the Standard & Poor's 500 Index (S&P 500) is trading at 2,795 June 2. An investor believes the S&P 500 will trade above 2,800 before the end of the trading day June 4. The trader purchases 10 S&P 500 options at a strike price of 2,800 options for $40 per contract.

Scenario 1:
***********
The S&P 500 closes above 2,800 at the end of the trading day, June 4. The investor is paid $100 per contract, which is a profit of $60 per contract or $600 (($100 - $40) x 10 contracts).

Scenario 2:
***********
The S&P 500 closes below 2,800 June 4. The investor loses all of the premium amount or $400 ($40 x 10 contracts).

Real World Example of a Bearish Digital Option
##############################################
Let's say gold is currently trading at $1,251, and an investor believes the price of gold will decline and close below $1,250 by the end of the day.

The investor sells a digital option for gold at a $1,250 strike price with expiry at the end of the day and will be paid $65 at expiry if correct. Since each of these digital options have a maximum value of $100, the premium paid in the event of a loss will be $35 or ($100 - $65).

Scenario 1:
***********
Gold's price falls and is trading at $1,150 by the end of the day. The investor is paid $65 for the option.

Scenario 2:
***********
The investor is wrong, and gold's price surges to $1,300 by the end of the day. The investor loses $35 or ($100 - $65 = $35).

Summary
-------
The trading of USD major pairings in the run up to the 2014 midterm election and the 2012 presidential election can be useful when examining just how
different USD valuations can behave when facing different election-year situations. Essentially, forex traders and investors can behave in nearly unpredictable ways when faced with the uncertainty of an election's outcome. Sometimes they are content to sit and wait, while other times the trading opportunity appears too good to pass up.
The tool gives investors an opportunity to make more Accurate bets on the FX market through 
it's Data-Analytical Algorithms.

.. .. code-block:: python

..     from quantdom import AbstractStrategy, Order, Portfolio

..     class ThreeBarStrategy(AbstractStrategy):

..         def init(self, high_bars=3, low_bars=3):
..             Portfolio.initial_balance = 100000  # default value
..             self.seq_low_bars = 0
..             self.seq_high_bars = 0
..             self.signal = None
..             self.last_position = None
..             self.volume = 100  # shares
..             self.high_bars = high_bars
..             self.low_bars = low_bars

..         def handle(self, quote):
..             if self.signal:
..                 props = {
..                     'symbol': self.symbol,  # current selected symbol
..                     'otype': self.signal,
..                     'price': quote.open,
..                     'volume': self.volume,
..                     'time': quote.time,
..                 }
..                 if not self.last_position:
..                     self.last_position = Order.open(**props)
..                 elif self.last_position.type != self.signal:
..                     Order.close(self.last_position, price=quote.open, time=quote.time)
..                     self.last_position = Order.open(**props)
..                 self.signal = False
..                 self.seq_high_bars = self.seq_low_bars = 0

..             if quote.close > quote.open:
..                 self.seq_high_bars += 1
..                 self.seq_low_bars = 0
..             else:
..                 self.seq_high_bars = 0
..                 self.seq_low_bars += 1

..             if self.seq_high_bars == self.high_bars:
..                 self.signal = Order.BUY
..             elif self.seq_low_bars == self.low_bars:
..                 self.signal = Order.SELL


.. Documentation
.. -------------

.. In progress ;)


.. TODO
.. ----

.. * Add integration with `TA-Lib <http://ta-lib.org/>`_
.. * Add the ability to use TensorFlow/CatBoost/Scikit-Learn and other ML tools to create incredible algorithms and strategies. Just as one of the first tasks is Elliott Wave Theory(Principle) - to recognize of current wave and on the basis of this predict price movement at confidence intervals
.. * Add the ability to make a sentiment analysis from different sources (news, tweets, etc)
.. * Add ability to create custom screens, ranking functions, reports


.. Contributing
.. ------------

.. * Fork it: https://github.com/constverum/Quantdom/fork
.. * Create your feature branch: git checkout -b my-new-feature
.. * Commit your changes: git commit -am 'Add some feature'
.. * Push to the branch: git push origin my-new-feature
.. * Submit a pull request!


.. Disclaimer
.. ----------

.. This software should not be used as a financial advisor, it is for educational use only.
.. Absolutely no warranty is implied with this product. By using this software you release the author(s) from any liability regarding the use of this software. You can lose money because this program probably has some errors in it, so use it at your own risk. And please don't take risks with money you can't afford to lose.


Feedback
--------

I'm very interested in your experience with this tool.
Please feel free to send me any feedback, ideas, enhancement requests or anything else.


.. License
.. -------

.. Licensed under the Apache License, Version 2.0
