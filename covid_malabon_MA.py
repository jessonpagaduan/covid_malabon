# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:51:59 2020

@author: Jesson Pagaduan
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize']=(20,10)
plt.rcParams['xtick.labelsize']='x-large'
plt.rcParams['ytick.labelsize']='x-large'
plt.style.use('ggplot')

df = pd.read_csv(r'C:\Users\Jesson Pagaduan\Google Drive\Data Viz\COVID_malabon\covid_malaboncity.csv')

df.date = pd.to_datetime(df.date)
df.set_index('date', inplace=True)

fig, ax = plt.subplots()
ax.plot(df.moveave, label='New cases', color='blue')
ax.plot(df.moveave_deaths, label='Deaths', color='red')
ax.plot(df.moveave_recovered, label='Recoveries', color='green')
ax.vlines(df.index[45], 0, 15, color='gray', linestyles='dashed')
ax.text(df.index[45], 10, 'Start of MECQ', rotation=90, verticalalignment='center', fontsize=25, color='gray')
ax.vlines(df.index[61], 0, 15, color='gray', linestyles='dashed')
ax.text(df.index[61], 10, 'Start of GCQ', rotation=90, verticalalignment='center', fontsize=25, color='gray')


ax.set_title('COVID-19 New Cases, Deaths, and Recoveries in Malabon City (as of June 9, 2020)', size=27)
ax.legend(fontsize=23, loc='upper left')
ax.annotate('Note: New cases, deaths, and recoveries are expressed in terms of 7-day moving averages.', (0,0), (10,-50), fontsize=15, 
             xycoords='axes fraction', textcoords='offset points', va='top')

ax.annotate('Source: Data compiled from daily reports of 100% Pusong Malabon Facebook Page (accessed June 9, 2020).', (0,0), (10,-70), fontsize=15, 
             xycoords='axes fraction', textcoords='offset points', va='top')
