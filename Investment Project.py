# -*- coding: utf-8 -*-

#pip install yfinance
#pip install yahoofinancials

# ~Imports for coding~  #
import numpy as np
import pandas as pd
import quandl as qd
import statsmodels.api as sm
import pandas_datareader
import datetime as dt
import pandas_datareader.data as web
import mysql.connector
import matplotlib.pyplot as plt 
%matplotlib inline
import csv
import yfinance as yf
import quandl
#Testing Area#
#Group 1 Short Term Long
group1_list=['SPY', 'XLB', 'XLY', 'XLV']
group2_list=['SPY', 'XLE', 'XLF', 'XLU', 'IYR' ]
group3_list=['SPY', 'VOX', 'XLK', 'XLP']


ax=
'''Great Recession'''
group1_rec = yf.download(group1_list, '2008-01-01', '2012-01-01')
group2_rec = yf.download(group2_list,'2008-01-01', '2012-01-01')
group3_rec = yf.download(group3_list, '2008-01-01', '2012-01-01')


#daily returns
group1_rec_returns=group1_rec["Adj Close"].pct_change(1)
group2_rec_returns=group2_rec["Adj Close"].pct_change(1)
group3_rec_returns=group3_rec["Adj Close"].pct_change(1)

group1_rec_cumret=(1+group1_rec_returns).cumprod
group2_rec_cumret=(1+group2_rec_returns).cumprod
group3_rec_cumret=(1+group3_rec_returns).cumprod

#Graphs
group1_rec["Adj Close"].plot(figsize=(25,15), grid=True)
group2_rec["Adj Close"].plot(figsize=(25,15), grid=True)
group3_rec["Adj Close"].plot(figsize=(25,15), grid=True)
#Covid Drop
data = yf.download(group1_list, '2018-01-01', '2022-01-01')
data["Adj Close"].plot(figsize=(25,15), grid=True)
data = yf.download(group2_list,'2018-01-01', '2022-01-01')
data["Adj Close"].plot(figsize=(25,15), grid=True)
data = yf.download(group3_list, '2018-01-01', '2022-01-01')
data["Adj Close"].plot(figsize=(25,15), grid=True)

#recent
data = yf.download(group1_list, '2021-01-01', '2022-04-16')
data["Adj Close"].plot(figsize=(25,15), grid=True)
data = yf.download(group2_list,'2021-01-01', '2022-04-16')
data["Adj Close"].plot(figsize=(25,15), grid=True)
data = yf.download(group3_list, '2021-01-01', '2022-04-16')
data["Adj Close"].plot(figsize=(25,15), grid=True)
'''
Tier 1:
20% + 
Consumer Cyclical
stocklist=["MCD", "HD", "DKS", "NKE", "TJX"]
Industrials & Comm Deff
stocklist=["MLI","HCKT", "DLTR", "DG","CRM"]

Tier 2:
15-20%
stocklist=["CVCO", "ACN", "SJM", "GIS", "QCOM", "KLA"]
'''



'''Testing Area
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open','MA50','MA200']].plot(label='gm',figsize=(16,8))
'''
'''
Upgrading Graphs
data = yf.download(group1_list, '2008-01-01', '2012-01-01')
data["Adj Close"].plot(figsize=(25,15), grid=True)
legend(['Basic Mats', ' Consumer Cycl', 'Healthcare', 'Industrials'])
data = yf.download(group2_list,'2008-01-01', '2012-01-01')
https://towardsdatascience.com/the-easiest-way-to-pull-stock-data-into-your-python-program-yfinance-82c304ae35dc
https://stackoverflow.com/questions/58387731/plotting-month-year-as-x-ticks-in-matplotlib
https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html
'''
    
stockList=["SJM", "GIS", "CLX",  "XLK", "QCOM", "NVDA",  "KLA", "CRM",  "TXN"]
for stock in stockList:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    log_ret= np.sum(np.log(data/data.shift()),axis=1)
    SR =log_ret.mean()/log_ret.std()
    print (stock + ' ' + str(SR))


stockList=["SJM", "GIS", "CLX",  "XLK", "QCOM", "NVDA",  "KLA", "CRM",  "TXN"]
for stock in stockList:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    price_data=data['Adj Close']
    ret_data= price_data.pct_change()
    cum_ret=(ret_data +1).cumprod() -1
    tot_cumret= cum_ret *100
    print(stock +str(tot_cumret))

stockList=["SJM", "GIS", "CLX",  "XLK", "QCOM", "NVDA",  "KLA", "CRM",  "TXN"]
for stock in stockList:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    price_data=data['Adj Close']
    ret_data= price_data.pct_change()
    ann_ret=ret_data.mean() *255
    print (stock+ ' '+ str(ann_ret))
ann_ret



tickers=["XLI", "EFX", "TRU","HCKT",  "MLI", "ACN", "ESAB", "KLA", "XLP",	"PG",	"DEO",	"WMT",	"COKE",	"DLTR",	"DG",	"TGT", "XLV",	"JNJ",	"PFE",	"TMO",	"CVS", "XLY",	"MCD",	"HD",	"LOW",	"DKS",	"NKE",	"GM",	"CVCO",	"TJX",	"Tol"]
for stock in tickers:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    log_ret= np.sum(np.log(data/data.shift()),axis=1)
    SR =log_ret.mean()/log_ret.std()
    print (stock + ' ' + str(SR))

for stock in tickers:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    price_data=data['Adj Close']
    ret_data= price_data.pct_change()
    ann_ret=ret_data.mean() *255
    print (stock+ ' '+ str(ann_ret))
    ann_ret
    
for stock in tickers:
    data = yf.download(stock, '2008-03-01', '2012-01-01')
    price_data=data['Adj Close']
    ret_data= price_data.pct_change()
    cum_ret=(ret_data +1).cumprod() -1
    tot_cumret= cum_ret *100
    print(stock +str(tot_cumret))