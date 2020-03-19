import os
import csv
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
sns.set()


################
# SIMPLE PARSING
################

files = ['Confirmed', 'Deaths', 'Recovered']

for s in files:
	temp = pd.read_csv('./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-'+s+'.csv') 
	temp = temp.drop('Lat', axis=1)
	temp = temp.drop('Long', axis=1)
	temp = temp.sort_values(by=['Country/Region'])
	temp = temp[~temp['Province/State'].str.contains(',', na=False)]
	temp = temp.groupby(['Country/Region']).sum()
	temp = temp.transpose()
	temp['date'] = pd.date_range(start='22/1/2020', periods=len(temp), freq='D')
	if s == 'Confirmed':
		confirmed = temp
	elif s == 'Deaths':
		deaths = temp
	elif s == 'Recovered':
		recovered = temp

print(confirmed['Canada'])
print(deaths)
print(recovered)

################
# SIMPLE PLOTTING
################

continents = ['Asia', 'Europe', 'Americas', 'Africa', 'Oceania and others']
countries = [	'China',		'Italy',			'US',			'South Africa',		'Australia', \
				'Korea, South',	'Spain',			'Canada',		'Egypt',			'New Zealand', \
				'Japan',		'France',			'Mexico',		'Algeria',			'Malaysia', \
				'Iran',			'Germany',			'Brazil',		'Morocco',			'Switzerland', \
				'India',		'United Kingdom',	'Argentina',	'Congo (Kinshasa)',	'Russia']

fig, axs = plt.subplots(5,5)

for i in range(len(countries)):
	ax = axs[int(i/5), i%5]
	if i<5:
		ax.set_title(continents[i] + '\n' + countries[i], fontsize=10)
	else: 
		ax.set_title(countries[i], fontsize=10)
	confirmed.plot('date', countries[i], ax=ax, legend=False)
	deaths.plot('date', countries[i], ax=ax, legend=False)
	recovered.plot('date', countries[i], ax=ax, legend=False)
	ax.set_xlabel('')
	ax.tick_params(axis='both', which='both', labelsize=6)
	if i < 20:
		ax.set_xticks([], minor=True)

plt.show()



