import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objects as update
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import ipywidgets as widgets
import numpy as np
import pandas as pd
import textwrap

from ipywidgets import interact, interact_manual
import IPython.display
from IPython.display import display, clear_output
import csv
import mysql.connector
import pandas as pd
from mysql.connector import Error
mydb = mysql.connector.connect(host='localhost',
                                         database='btc',
                                         user='root',
                                         password='Trigma#2020')
cursor = mydb.cursor()
query = "Select * from crypto;"
dataframe = pd.read_sql(query,mydb)



df = dataframe.loc[dataframe['symbol'] == 'ADA/USDT']
df1= dataframe.loc[dataframe['symbol'] == 'BNB/USDT']

df2 = dataframe.loc[dataframe['symbol'] == 'BTC/USDT']
df3 = dataframe.loc[dataframe['symbol'] == 'DOGE/USDT']

df4= dataframe.loc[dataframe['symbol'] == 'ETH/USDT']
df5 = dataframe.loc[dataframe['symbol'] == 'XRP/USDT']


'''
df = pd.read_csv('/home/kkr/Downloads/crypto/Binance_ADAUSDT_d.csv')

df1 = pd.read_csv('/home/kkr/Downloads/crypto/Binance_BNBUSDT_d.csv')
df2 = pd.read_csv('/home/kkr/Downloads/crypto/Binance_BTCUSDT_d.csv')
df3 = pd.read_csv('/home/kkr/Downloads/crypto/Binance_DOGEUSDT_d.csv')
df4 = pd.read_csv('/home/kkr/Downloads/crypto/Binance_ETHUSDT_d.csv')
df5 = pd.read_csv('/home/kkr/Downloads/crypto/Binance_LTCUSDT_d.csv')
'''




ADA = go.Figure(data=[go.Candlestick(x=df['date'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'])])
ADA.update_xaxes(title_text='date')
ADA.update_yaxes(title_text='volume')
#fig.show()

BNB= go.Figure(data=[go.Candlestick(x=df1['date'],
    open=df1['open'],
    high=df1['high'],
    low=df1['low'],
    close=df1['close'])])
BNB.update_xaxes(title_text='date')
BNB.update_yaxes(title_text='volume')
#fig1.show()


BTC = go.Figure(data=[go.Candlestick(x=df2['date'],
    open=df2['open'],
    high=df2['high'],
    low=df2['low'],
    close=df2['close'])])
BTC.update_xaxes(title_text='Date')
BTC.update_yaxes(title_text='volume')
#BTC.show()

DOGE = go.Figure(data=[go.Candlestick(x=df3['date'],
    open=df3['open'],
    high=df3['high'],
    low=df3['low'],
    close=df3['close'])])
DOGE.update_xaxes(title_text='date')
DOGE.update_yaxes(title_text='volume')
#DOGE.show()

ETH = go.Figure(data=[go.Candlestick(x=df4['date'],
    open=df4['open'],
    high=df4['high'],
    low=df4['low'],
    close=df4['close'])])
ETH.update_xaxes(title_text='date')
ETH.update_yaxes(title_text='volume')
#ETH.show()

LTC = go.Figure(data=[go.Candlestick(x=df5['date'],
    open=df5['open'],
    high=df5['high'],
    low=df5['low'],
    close=df5['close'])])
LTC.update_xaxes(title_text='date')
LTC.update_yaxes(title_text='volume')
#LTC.show()



updatemenus = [{
#                 'active':1,
                'buttons': [{'method': 'update',
                             'label': 'ADA',
                             'args': [
                                      # 1. updates to the traces
                                      {'open': [list(df.open)],
                                       'high': [list(df.high)],
                                       'low': [list(df.low)],
                                       'close': [list(df.close)],
                                       'x':[list(df.date)],
                                       'visible': True}, 
                                      
                                      # 2. updates to the layout
                                      {'title':'ADA'},
                                      
                                      # 3. which traces are affected 
#                                       [0, 1],
                                      
                                      ],  },
                            {'method': 'update',
                             'label': 'BNB', 
                             'args': [
                                       # 1. updates to the traces  
                                       {'open': [list(df1.open)],
                                        'high': [list(df1.high)],
                                        'low': [list(df1.low)],
                                        'close': [list(df1.close)],
                                        'x':[list(df1.date)],
                                       'visible': True},
                                      
                                       # 2. updates to the layout
                                       {'title':'BNB'},
                                       
                                       # 3. which traces are affected
#                                        [0, 1]
                                      ]
                            
                            },
                            {'method': 'update',
                             'label': 'BTC', 
                             'args': [
                                       # 1. updates to the traces  
                                       {'open': [list(df2.open)],
                                        'high': [list(df2.high)],
                                        'low': [list(df2.low)],
                                        'close': [list(df2.close)],
                                        'x':[list(df2.date)],
                                       'visible': True},
                                      
                                       # 2. updates to the layout
                                       {'title':'BTC'},
                                       
                                       # 3. which traces are affected
#                                        [0, 1]
                                      ]
                            
                            },
                            {'method': 'update',
                             'label': 'DOGE', 
                             'args': [
                                       # 1. updates to the traces  
                                       {'open': [list(df3.open)],
                                        'high': [list(df3.high)],
                                        'low': [list(df3.low)],
                                        'close': [list(df3.close)],
                                        'x':[list(df3.date)],
                                       'visible': True},
                                      
                                       # 2. updates to the layout
                                       {'title':'DOGE'},
                                       
                                       # 3. which traces are affected
#                                        [0, 1]
                                      ]},
                            {'method': 'update',
                             'label': 'ETH', 
                             'args': [
                                       # 1. updates to the traces  
                                       {'open': [list(df4.open)],
                                        'high': [list(df4.high)],
                                        'low': [list(df4.low)],
                                        'close': [list(df4.close)],
                                        'x':[list(df4.date)],
                                       'visible': True},
                                      
                                       # 2. updates to the layout
                                       {'title':'ETH'},
                                       
                                       # 3. which traces are affected
#                                        [0, 1]
                                      ]  },
                            {'method': 'update',
                             'label': 'XRP', 
                             'args': [
                                       # 1. updates to the traces  
                                       {'open': [list(df5.open)],
                                        'high': [list(df5.high)],
                                        'low': [list(df5.low)],
                                        'close': [list(df5.close)],
                                        'x':[list(df5.date)],
                                       'visible': True},
                                      
                                       # 2. updates to the layout
                                       {'title':'XRP'},
                                       
                                       # 3. which traces are affected
#                                        [0, 1]
                                      ]
                             
                            
                            },],
                'type':'dropdown',
#                 'type':'dropdown',
                'direction': 'down',
                'showactive': True,}]

# update layout with buttons, and show the figure
ADA.update_layout(updatemenus=updatemenus)
