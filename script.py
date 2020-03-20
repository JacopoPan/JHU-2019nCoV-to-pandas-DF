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

# there are 3 time series files
files = ['Confirmed', 'Deaths', 'Recovered']

# for each one of them
for s in files:
	# read the CSV
	temp = pd.read_csv('./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-'+s+'.csv') 
	# drop latitute and longitude information
	temp = temp.drop('Lat', axis=1)
	temp = temp.drop('Long', axis=1)
	# sort by country
	temp = temp.sort_values(by=['Country/Region'])
	# remove the entires with a ',' in the 'Province/State' column
	# as of March 20, these are entires relative US counties
	# while I only want to consider the US states
	temp = temp[~temp['Province/State'].str.contains(',', na=False)]
	# sum lines relative to regions of a single country
	# i.e., Chinese provinces, Canadian provinces, US states, etc
	temp = temp.groupby(['Country/Region']).sum()
	# transpose the frame
	temp = temp.transpose()
	# add a 'date column'
	# as of March, 20 all series start on January, 22
	temp['date'] = pd.date_range(start='22/1/2020', periods=len(temp), freq='D')
	if s == 'Confirmed':
		confirmed = temp
	elif s == 'Deaths':
		deaths = temp
	elif s == 'Recovered':
		recovered = temp

# these 3 dataframes contain information
# about confirmed cases, deaths, and recovered patients
# for 155 countries over 58 (as of March 20) days
print(confirmed['Canada'])
print(deaths)
print(recovered)




################
# SIMPLE PLOTTING
################

# confirmed cases, deaths, and recovered patients for
# a selection of 5 countries for each of the 5 continents

continents = ['Asia', 'Europe', 'Americas', 'Africa', 'Oceania and others']
countries = [	'China',		'Italy',			'US',			'South Africa',		'Australia', \
				'Korea, South',	'Spain',			'Canada',		'Egypt',			'New Zealand', \
				'Japan',		'France',			'Mexico',		'Algeria',			'Malaysia', \
				'Iran',			'Germany',			'Brazil',		'Morocco',			'Switzerland', \
				'India',		'United Kingdom',	'Argentina',	'Congo (Kinshasa)',	'Russia']

fig, axs = plt.subplots(5,5)

for i in range(len(countries)):
	# get axis
	ax = axs[int(i/5), i%5]
	# set title
	if i<5:
		ax.set_title(continents[i] + '\n' + countries[i], fontsize=10)
	else: 
		ax.set_title(countries[i], fontsize=10)
	# plot
	confirmed.plot('date', countries[i], ax=ax, legend=False)
	deaths.plot('date', countries[i], ax=ax, legend=False)
	recovered.plot('date', countries[i], ax=ax, legend=False)
	# label and ticks options
	ax.set_xlabel('')
	ax.tick_params(axis='both', which='both', labelsize=6)
	# only plot the x ticks for the last row of plots
	if i < 20:
		ax.set_xticks([], minor=True)

plt.show()

