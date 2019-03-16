import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# First, we retrieve data: 
# start = dt.datetime(2015, 1, 1)
# end = dt.datetime.now()
# df = web.DataReader("TSLA", 'iex', start, end)

# normally we need to manually set the index, but in this case it's already done:
# df.reset_index(inplace=True)
# df.set_index("date", inplace=True)
# print(df.head())


# Then save as a CSV:
# df.to_csv('tsla.csv')

# Now read the CSV and plot a graph of closing prices:
df = pd.read_csv('./tsla.csv', parse_dates=True, index_col=0)

df['close'].plot()
print("Stock price graph of Tesla has been loaded")
plt.show()

