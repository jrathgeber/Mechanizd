# Mechanizd

This project contains the source code to genrate http://www.Mechanizd.com

Mechanizd is a site for displaying the status of various algorithmic trading strategies that I run in live, paper and backetst modes. The python code automates the running of the Zorro and RightEdge Algorithmic tools and extracts data from reports generated to populate the web site daily. Also handled is batch scheduling and web site scraping.

Work in progress includes connection the Interactive Brokers Python API and some basic ml decision trees with Scikitlearn.

## Table of Contents
- [batch](#batch)
- [ib](#ib)
- [maxalpha](#maxalpha)
- [ml](#ml)
- [rightedge](#rightedge)
- [zorro](#zorro)

## Batch
* [Batch7pmSun](/batch/Batch7pmSun.py)
* [BatchMktClose](/batch/BatchMktClose.py)
* [BatchOptimise](/batch/BatchOptimise.py)
* [Batch_Weekday](/batch/Batch_Weekday.py)
* [sendMail](/batch/sendMail.py)
## ib
* [hello_world](/ib/hello_world.py)
## maxalpha
* [Batch](/maxalpha/Batch.py)
* [BatchOp](/maxalpha/BatchOp.py)
* [FileReadingRE](/maxalpha/FileReadingRE.py)
* [MaxAlpha](/maxalpha/MaxAlpha.py)
* [Maxalpha2](/maxalpha/Maxalpha2.py)
* [Optimise](/maxalpha/Optimise.py)
* [Pg](/maxalpha/Pg.py)
* [RightEdge](/maxalpha/RightEdge.py)
* [SymbolConfig](/maxalpha/SymbolConfig.py)
## ml
* [es_mini_tree](/ml/es_mini_tree.py)
* [plot_confusion](/ml/plot_confusion.py)
* [ts_feature_extraction](/ml/ts_feature_extraction.py)
## rightedge
* [FileReadingRE](/rightedge/FileReadingRE.py)
* [RightEdge](/rightedge/RightEdge.py)
* [RightEdgeIB](/rightedge/RightEdgeIB.py)
* [RightEdgeIBFull](/rightedge/RightEdgeIBFull.py)
## zorro
* [BatchZorroMech0](/zorro/BatchZorroMech0.py)
* [BatchZorroMech1](/zorro/BatchZorroMech1.py)
* [BatchZorroMech2](/zorro/BatchZorroMech2.py)
* [FileReadingBackTest](/zorro/FileReadingBackTest.py)
* [backtest](/zorro/backtest.py)
* [train](/zorro/train.py)

