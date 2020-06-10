# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:45:34 2020

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
ax.bar(df.index, df.new_cases, alpha=0.2, color='green', label='New cases')
ax.plot(df.moveave, label='7-day moving average')
ax.vlines(df.index[45], 0, 23, color='gray', linestyles='dashed')
ax.text(df.index[45], 15, 'Start of MECQ', rotation=90, verticalalignment='center', fontsize=25, color='gray')
ax.vlines(df.index[61], 0, 23, color='gray', linestyles='dashed')
ax.text(df.index[61], 15, 'Start of GCQ', rotation=90, verticalalignment='center', fontsize=25, color='gray')


ax.set_title('COVID-19 Cases in Malabon City (as of June 9, 2020)', size=30)
ax.legend(fontsize=25)
ax.annotate('Source: Data compiled from daily reports of 100% Pusong Malabon Facebook Page (accessed June 9, 2020).', (0,0), (10,-40), fontsize=15, 
             xycoords='axes fraction', textcoords='offset points', va='top')
