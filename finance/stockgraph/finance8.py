import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle       # so you can save objects
import requests    
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

def visualize_data():
    df = pd.read_csv('ftse250_joinedcloses.csv')
    # df['AGK'].plot()
    # plt.show() # example plot
    df_corr = df.corr()     # calculates correlation values in a correlation table
    # return df_corr.head()   # two highly correlated companies that deviate are likely to "come back together"
                            # non-correlated stocks show diversified portfolio
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) # 1 x 1, plot number 1

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn) #RedYellowGreen range
    fig.colorbar(heatmap)
    
    # plot colors on a grid, then we need to know which companies are where
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False) # +0.5 for halfway through square
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis() # put y on side and invert
    ax.xaxis.tick_top() # put x on top as it's basically a table

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)

    # need to set xticks to vertical
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1) # set the range for the heatmap range
    plt.tight_layout()
    plt.show()

# visualize the data:
visualize_data()