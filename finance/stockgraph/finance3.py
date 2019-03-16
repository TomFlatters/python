import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# 100 day moving average:
df['100ma'] = df['close'].rolling(window=100, min_periods=0).mean()

print(df.head()) # note that the first 100 data points will not have a moving average available!

# df.dropna(inplace=True) # let's drop the NaN data

# df['100ma'].plot()
# plt.show()

# subplots with matplotlib:
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['volume'])

plt.show()