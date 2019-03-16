import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle       # so you can save objects
import requests    

# yahoo is deprecated
import fix_yahoo_finance as yf

# import prev. function
from finance5 import save_ftse250_tickers

# get data from yahoo:
def get_data_from_yahoo(reload_sp500=False):        # could add another "reloaddata" parameter ?
    if reload_sp500:
        tickers = save_ftse250_tickers()
    else:
        with open("ftse250tickers.pickle","rb") as f:
            tickers = pickle.load(f)        # create tickers list
    
    # we should store all the data locally in order to reduce pull times: (500MB!)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = "2000-1-1"
    end = "2019-3-14"

    for ticker in tickers[200:]:
        print(ticker)
        # note: will get errors if run this because 
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            yf.pdr_override()
            try:
                df = yf.download(ticker+'.L', start=start, end=end)
                df.reset_index(inplace=True)
                df.set_index("Date", inplace=True)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            except:
                print("Ticker invalid: " + ticker)
                pass
            
        else:
            print('Already have {}'.format(ticker))
    

get_data_from_yahoo()

