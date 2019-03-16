import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# resampling data - we get daily data, but we will resample to 10 day data, this is 
# suitable for scaling UP from any timeframe

df_ohlc = df['close'].resample('10D').ohlc() # not a moving average, but ohlc uses adjusted close etc which is very useful for stock splits.
df_volume = df['volume'].resample('10D').sum()

# reset the index so date is now a column - for the candlestick_ohlc usage:
df_ohlc.reset_index(inplace=True)

df_ohlc['date'] = df_ohlc['date'].map(mdates.date2num) # convert to mdate number

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()