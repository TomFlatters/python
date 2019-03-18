import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle       # so you can save objects
import requests    

def compile_data():
    with open("ftse250tickers.pickle","rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers): # for each item in tickers
        try:
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        except:
            continue
        df.set_index('Date', inplace=True)

        df.rename(columns = {'Adj Close': ticker}, inplace = True)
        df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            try:
                main_df = main_df.join(df, how='outer')
            except:
                pass
        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv('ftse250_joinedcloses.csv')

compile_data()