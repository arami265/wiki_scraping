import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def bar_plot(df):
    plt.subplots(figsize=(20, 15))
    df = df.truncate(after=100)
    sns.set()
    g = sns.barplot(x='word', y='freq', data=df)

    max_freq = df['freq'].max()

    if max_freq > 40:
        y_tick_freq = int(max_freq / 40)
    else:
        y_tick_freq = 2

    # For now this is sort of a hack to get the max value to match closely with the max y tick.
    # If even, the ticks are even, etc.
    if max_freq % 2 == 0:
        y_tick_start = 2
    else:
        y_tick_start = 1

    g.set(yticks=np.arange(y_tick_start, max_freq + 1, y_tick_freq))
    plt.xticks(rotation=90)
    plt.show()
