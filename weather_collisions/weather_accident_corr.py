"""Author: Akash Shah

This script loads various data on weather conditions, as well as accidents during those weather conditions and analyzes
possible correlations between them. The accident frequencies are normalized by the underying frequency of the weather condition.

"""

import numpy as np
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import warnings

def temp_accidents_corr():
	#first column is counts, second is temperature
	temp_accidents = np.loadtxt('output/temp_and_accident_frequency.tsv',delimiter='\t',skiprows=1)

	#first column is temperature, second is counts
	temp_distribution = np.loadtxt('../weather/output/temperature_distribution.tsv',delimiter='\t',skiprows=1)

	#normalize counts by frequency of temperature event
	normalized_accidents = temp_accidents[:,0]/temp_distribution[:,1]

	print "Correlation between temperature and accidents: " + str(pearsonr(normalized_accidents,temp_accidents[:,1])[0])
	print "Correlation between log of temperature and accidents: " + str(pearsonr(normalized_accidents,np.log(temp_accidents[:,1]+1))[0]) +'\n'

	return pearsonr(normalized_accidents,temp_accidents[:,1])[0]

def temp_accident_types_corr():
	#first four columns are pedestrian/cyclist injuries/deaths, last is temperature
	temp_accident_types = np.loadtxt('output/temp_and_pedestrian_cyclist_accidents.tsv',delimiter='\t',skiprows=1)

	#first column is temperature, second is counts
	temp_distribution = np.loadtxt('../weather/output/temperature_distribution.tsv',delimiter='\t',skiprows=1)

	print "Correlation between pedestrian injuries and temp: " + str(pearsonr(temp_accident_types[:,0]/temp_distribution[:,1],temp_accident_types[:,4])[0])
	print "Correlation between pedestrian injuries and log of temp: " + str(pearsonr(temp_accident_types[:,0]/temp_distribution[:,1],np.log(temp_accident_types[:,4]+1))[0])

	print "Correlation between pedestrian deaths and temp: " + str(pearsonr(temp_accident_types[:,1]/temp_distribution[:,1],temp_accident_types[:,4])[0])
	print "Correlation between pedestrian deaths and log of temp: " + str(pearsonr(temp_accident_types[:,1]/temp_distribution[:,1],np.log(temp_accident_types[:,4]+1))[0])

	print "Correlation between cyclist injuries and temp: " + str(pearsonr(temp_accident_types[:,2]/temp_distribution[:,1],temp_accident_types[:,4])[0])
	print "Correlation between cyclist injuries and log of temp: " + str(pearsonr(temp_accident_types[:,2]/temp_distribution[:,1],np.log(temp_accident_types[:,4]+1))[0])

	print "Correlation between cyclist deaths and temp: " + str(pearsonr(temp_accident_types[:,3]/temp_distribution[:,1],temp_accident_types[:,4])[0])
	print "Correlation between cyclist deaths and log of temp: " + str(pearsonr(temp_accident_types[:,3]/temp_distribution[:,1],np.log(temp_accident_types[:,4]+1))[0])+'\n'

def precip_1hr_accidents_corr():
	precip_1hr_accidents = np.loadtxt('output/accidents_by_precip1hr.tsv',delimiter='\t',skiprows=1)

	precip_distribution = np.loadtxt('../weather/output/precip_1hr_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with precipitation values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(precip_distribution)) if precip_distribution[i,0] not in precip_1hr_accidents[:,0]]
	precip_distribution = np.delete(precip_distribution,rows_to_remove,0)

	print "Correlation between 1 hr precip and accidents: " + str(pearsonr(precip_1hr_accidents[:,0],precip_1hr_accidents[:,1]/precip_distribution[:,1])[0]) +'\n'

	return pearsonr(precip_1hr_accidents[:,0],precip_1hr_accidents[:,1]/precip_distribution[:,1])[0]

def cc_accidents_corr():
	cc_accidents = np.loadtxt('output/accidents_by_cloud_ceiling.tsv',delimiter='\t',skiprows=1)

	cc_distribution = np.loadtxt('../weather/output/cloud_ceiling_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with cloud ceiling values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(cc_distribution)) if cc_distribution[i,0] not in cc_accidents[:,0]]
	cc_distribution = np.delete(cc_distribution,rows_to_remove,0)

	print "Correlation between cloud ceiling and accidents: " + str(pearsonr(cc_accidents[:,0],cc_accidents[:,1]/cc_distribution[:,1])[0]) +'\n'

	return pearsonr(cc_accidents[:,0],cc_accidents[:,1]/cc_distribution[:,1])[0]

def visibility_accidents_corr():
	#first row is counts, second row is visibility measure
	visibility_accidents = np.loadtxt('output/visibility_and_accident_frequency.tsv',delimiter='\t',skiprows=1)

	visibility_distribution = np.loadtxt('../weather/output/visibility_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with visbility values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(visibility_distribution)) if visibility_distribution[i,0] not in visibility_accidents[:,1]]
	visibility_distribution = np.delete(visibility_distribution,rows_to_remove,0)

	print "Correlation between visibility and accidents: " + str(pearsonr(visibility_accidents[:,0]/visibility_distribution[:,1],visibility_accidents[:,1])[0]) +'\n'

	return pearsonr(visibility_accidents[:,0]/visibility_distribution[:,1],visibility_accidents[:,1])[0]

def snow_depth_accidents_corr():
	snow_depth_accidents = np.loadtxt('output/accidents_by_snow_depth.tsv',delimiter='\t',skiprows=1)

	snow_depth_distribution = np.loadtxt('../weather/output/snow_depth_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with snow depth values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(snow_depth_distribution)) if snow_depth_distribution[i,0] not in snow_depth_accidents[:,0]]
	snow_depth_distribution = np.delete(snow_depth_distribution,rows_to_remove,0)

	print "Correlation between snow depth and accidents: " + str(pearsonr(snow_depth_accidents[:,0],snow_depth_accidents[:,1]/snow_depth_distribution[:,1])[0]) +'\n'

	return pearsonr(snow_depth_accidents[:,0],snow_depth_accidents[:,1]/snow_depth_distribution[:,1])[0]

def wind_speed_accidents_corr():
	wind_speed_accidents = np.loadtxt('output/accidents_by_wind_speed.tsv',delimiter='\t',skiprows=1)

	wind_speed_distribution = np.loadtxt('../weather/output/wind_speed_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with snow depth values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(wind_speed_distribution)) if wind_speed_distribution[i,0] not in wind_speed_accidents[:,0]]
	wind_speed_distribution = np.delete(wind_speed_distribution,rows_to_remove,0)


	print "Correlation between wind speed and accidents: " + str(pearsonr(wind_speed_accidents[:,0],wind_speed_accidents[:,1]/wind_speed_distribution[:,1])[0]) +'\n'

	return pearsonr(wind_speed_accidents[:,0],wind_speed_accidents[:,1]/wind_speed_distribution[:,1])[0]

def gust_accidents_corr():
	gust_accidents = np.loadtxt('output/accidents_by_gust.tsv',delimiter='\t',skiprows=1)

	gust_distribution = np.loadtxt('../weather/output/gust_distribution.tsv',delimiter='\t',skiprows=1)

	#remove rows with snow depth values in underlying distribution that don't appear in accidents
	rows_to_remove = [i for i in range(len(gust_distribution)) if gust_distribution[i,0] not in gust_accidents[:,0]]
	gust_distribution = np.delete(gust_distribution,rows_to_remove,0)

	print "Correlation between gust and accidents: " + str(pearsonr(gust_accidents[:,0],gust_accidents[:,1]/gust_distribution[:,1])[0]) +'\n'

	return pearsonr(gust_accidents[:,0],gust_accidents[:,1]/gust_distribution[:,1])[0]

def plot_correlations(corr):
	"""plot pairwise correlations"""

	pos_corr = [corr[i] if corr[i]>=0 else 0 for i in range(len(corr))]
	neg_corr = [corr[i] if corr[i]<0 else 0 for i in range(len(corr))]

	plt.bar(np.arange(len(corr)),pos_corr,align='center',color='b',width=1.0)
	plt.bar(np.arange(len(corr)),neg_corr,align='center',color='r',width=1.0)

	#set labels, titles, and ticks with weather events
	plt.xlabel('Weather Conditions')
	plt.ylabel('Correlation with Accidents')
	tick_names = ['Temperature','1 Hr Precip','Cloud Ceiling','Visibility','Snow Depth','Wind Speed','Gust']
	plt.xticks(np.arange(len(pos_corr)), tick_names,fontsize=8)
	#plt.xticks(rotation=90)
	plt.title('Correlation of Weather Features with Number of Accidents')

	#catches user warning rather than printing it
	with warnings.catch_warnings():
		warnings.simplefilter("ignore", UserWarning)
		plt.tight_layout()

	plt.savefig('correlations.png')


temp_corr = temp_accidents_corr()

temp_accident_types_corr()

precip_corr = precip_1hr_accidents_corr()

cc_corr = cc_accidents_corr()

visibility_corr = visibility_accidents_corr()

snow_depth_corr = snow_depth_accidents_corr()

wind_speed_corr = wind_speed_accidents_corr()

gust_corr = gust_accidents_corr()

plot_correlations([temp_corr,precip_corr,cc_corr,visibility_corr,snow_depth_corr,wind_speed_corr,gust_corr])

