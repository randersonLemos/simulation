# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:07 2019

@author: randerson
"""


import matplotlib.pyplot as plt
import matplotlib.dates as mdates


locator = mdates.MonthLocator(bymonth=[1])
formatter = mdates.DateFormatter('%Y')


class Graph():
    @staticmethod
    def gas(ax, df, title):
        df = df/1000000
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$mmsm^3 std$')

    @staticmethod
    def gas_dot(ax, df, title):
        df = df/1000000
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$mmsm^3/d$')

    @staticmethod
    def fluid(ax, df, title):
        df = df/1000
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$msm^3 std$')

    @staticmethod
    def fluid_dot(ax, df, title):
        df = df/1000
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$msm^3/d$')

    @staticmethod
    def fluid_ratio(ax, df, title):
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$m^3/m^3$')
        ax.set_title(title)

    @staticmethod
    def percent(ax, df, title):
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('%')
        ax.set_title(title)

    @staticmethod
    def pressure(ax, df, title):
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$kg/m^2$')
        ax.set_title(title)

    @staticmethod
    def pressure_dot(ax, df, title):
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$kg/m^2/day$')
        ax.set_title(title)

    @staticmethod
    def show():
        plt.show()
