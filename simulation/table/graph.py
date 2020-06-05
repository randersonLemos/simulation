import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter

locator = mdates.MonthLocator(bymonth=[1])
formatter = mdates.DateFormatter('%Y')



class Graph():
    @staticmethod
    def gas(df, title, ax):
        df = df/1000000
        df.plot(ax=ax, x_compat=True)

        plt.style.use('seaborn-talk')
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$mmsm^3$')

        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=90, horizontalalignment='center')
        #ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_locator(LinearLocator(10))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.set_ylim(ymin=0)
        ax.grid()

    #@staticmethod
    #def gas_dot(ax, df, title):
    #    df = df/1000000
    #    df.plot(ax=ax, x_compat=True)
    #    plt.setp(ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
    #    ax.xaxis.set_major_locator(locator)
    #    ax.xaxis.set_major_formatter(formatter)
    #    ax.set_title(title)
    #    ax.set_xlabel('date')
    #    ax.set_ylabel('$mmsm^3/d$')

    @staticmethod
    def fluid(df, title, ax):
        df = df/1000
        df.plot(ax=ax, x_compat=True)

        plt.style.use('seaborn-talk')
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$msm^3$')

        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=90, horizontalalignment='center')
        #ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_locator(LinearLocator(10))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.set_ylim(ymin=0)
        ax.grid()

    @staticmethod
    def pressure(df, title, ax):
        df.plot(ax=ax, x_compat=True)

        plt.style.use('seaborn-talk')

        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$kg/cm^2$')

        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=90, horizontalalignment='center')
        #ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_locator(LinearLocator(10))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))
        ax.grid()
