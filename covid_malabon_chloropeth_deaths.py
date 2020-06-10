# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:31:30 2020

@author: Jesson Pagaduan
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fp = r'C:\Users\Jesson Pagaduan\Google Drive\Data Viz\COVID_malabon\malabon_GIS\malabon_metromanila.shp'

map_df = gpd.read_file(fp)
map_df.plot()

df = pd.read_csv(r'C:\Users\Jesson Pagaduan\Google Drive\Data Viz\COVID_malabon\covid_malabon_map_june9.csv')

merged = map_df.set_index('NAME_3').join(df.set_index('brgy'))

variable = 'deaths'

vmin, vmax = 0, 7

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')

ax.axis('off')

ax.set_title('COVID-19 Deaths in Malabon City (as of June 9, 2020)')
ax.annotate('Source: PhilGIS and data compiled from daily reports of 100% Pusong Malabon Facebook Page (accessed June 9, 2020).', xy=(0.10,0.05), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=8, color='#555555')

sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
