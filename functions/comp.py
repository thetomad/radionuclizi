import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def compare(data1, data2, x , y, x_label, y_label, first_label, second_label, location):
    data_1 = pd.read_csv(data1)
    data_2 = pd.read_csv(data2)

    plt.figure(figsize=(20, 10))
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')


    x_1 = data_1[x]
    x_2 = data_2[x]

    y_1 = data_1[y]
    y_2 = data_2[y]

    plt.plot(x_1,y_1,'o', label= first_label)
    plt.plot(x_2,y_2,'.', label= second_label)
    plt.legend(loc='lower right', prop={"size":20})

    plt.savefig(location)