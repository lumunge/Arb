## ARB

This is a CLI tool built with python and SQL which collects data from various betting sites and presents available arbitrage opportunities.

#### What is Arbitrage?

This is involves taking advantage of a difference in prices in financial markets or odds in sports betting where we find combinations that allow for capitalization on the differences.
In principle, an arbitrage is risk-free except in some cases where whereby prices or odds fluctuate or devaluation of a currency in the case of financial markets.
For more information this [link](https://en.wikipedia.org/wiki/Arbitrage) is helpful.

#### What is Arbitrage Betting?

This is an arbitrage that occurs in sports betting markets due to bookmakers having different opinions about the outcome of a sports event. In such cases, if the conditions allow, an arbitrage better can make a profit by placing a bet on each outcome with different betting sites.

An arbitrage opportunity occurs when there are a set of odds that present a mutually exclusive outcome that covers all state space possibilities whose implied probability adds up to less than 1 or 100%.
For more information this [link](https://en.wikipedia.org/wiki/Arbitrage_betting) is helpful.

Arbitrage bet in sports betting is an activity where a bettor simultaneously places bets on all possible outcomes of an event at odds that guarantee a profit, whatever the result of the event will be. A simple example of how this can be achieved is found here.

#### Project Dependencies:

- requests
- sqlite3
- urllib
- json

#### How to use it?

The scripts will fetch odds from the various betting sites and different leagues then print all odds in an organized manner in a bash terminal. Also, note that [termux](https://play.google.com/store/apps/details?id=com.termux) can be used to execute the scripts from an android phone. From the output, there will be probabilities highlighted in green color which are less than 100%. These are the arbitrage opportunities. Once the odds are printed this [Arbitrage calculator](https://thearbacademy.com/arbitrage-betting-calculator/) is useful to determine the stakes to place and profits. This code only covers 3-way bets so in the calculator the bettor has to place three bets(three odds).

1. To get started we execute the following script to download the source code to a local directory;

```
$ git clone https://github.com/lumunge/Arb.git
```

2. We make sure the repo is successfully downloaded.

3. We install all project requirements.

```
$ pip install -r requirements.txt
```

It is advisable to do this in a python virtual environment.
To create a virtual environment we write;

```
$ virtualenv [Name of virtual environment]
```

Once created we activate it as follows;

```
$ source [path to activation script]
```

To deactivate a python environment, we write;

```
$ deactivate
```

4. We are now ready to run the scripts.

- We first make sure all the shell scripts can be executed by providing appropriate permissions;

```
$ chmod +x *.sh
```

- Next we run the initialization script that creates json directories and databases with tables for data cleaning and processing(For this step to work make sure [sqlite3](https://linuxhint.com/install-sqlite-ubuntu-linux-mint/) in installed);

```
$ ./start_here.sh
```

If the above script executed successfully we execute the text "### SUCCESS!! ###" to be printed.

- To look for arbitrage opportunities in the Bundesliga execute the command;

```
$ ./runBL.sh
```

- For arbitrage opportunities in the premier league execute the command;

```
$ ./runPL.sh
```

- For opportunities in Series A league, execute the command;

```
$ ./runSA.sh
```

- For La Liga opportunities we write;

```
$ ./runLL/sh
```

- For all opportunities we write;

```
$ ./runLL/sh
```

Arbitrage opportunities are highlighted in a green color as shown below;

#### Disclaimer

This is intended purely as an experiment. I do not recommend that anyone pursue the arbitrage opportunities provided by this code with real money. There are many factors involved to ensure a profit such as tax, odds fluctuating, and much more. Also, bookmakers don't like to lose. That said, I will not be devoting any time to maintaining this repository, and as such bugs can present themselves and therefore challenge the authenticity of an arb. In addition to this, arbitrage betting is a risky endeavor even with the right data.

#### Closing thoughts.

This code is open-sourced for anyone to use for any purpose seen fit. Any contributions to the project are invited just create a pull request and we will proceed from there. For the purposes of implementing this work somewhere else, I kindly ask for credit.
