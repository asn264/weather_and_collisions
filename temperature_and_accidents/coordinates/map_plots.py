'''
Aditi Nair
May 2016

Plotting map projections for collisions involving cyclists in Brooklyn. 
'''

import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import sys

def load_data():

	coords_by_temp = {}

	with open('coords_and_temp_brooklyn_bike_deaths_and_injuries.tsv', 'rb') as doc:

		for line in doc:

			data = line.strip().split('\t')

			if data[-1] != 'NULL':
				if data[-1] in coords_by_temp:
					coords_by_temp[data[-1]][0].append(float(data[0]))
					coords_by_temp[data[-1]][1].append(float(data[1]))
				else:
					#Key for each temperature bucket: value is two lists, one for latitudes and the other for longitudes
					coords_by_temp[data[-1]] = [ [float(data[0])], [float(data[1])] ]
	
	key_values = [int(x) for x in list(coords_by_temp.keys())]
	return coords_by_temp, [str(x) for x in sorted(key_values)]

def plot_map():

	coords_by_temp, vals = load_data()

	fig, ax = plt.subplots(figsize=(12,10))

	r = 1
	for temp_bucket in vals:

		plt.subplot(2, 5, r)
		r += 1

		try:
			print temp_bucket
			bike_map = Basemap(projection='merc', lat_0=40.7, lon_0=-74.0, resolution = 'h', area_thresh = 0.1, \
			    llcrnrlon=-74.1, \
			    llcrnrlat=40.55, \
			    urcrnrlon=-73.9, \
			    urcrnrlat=40.85)

			bike_map.drawcoastlines()
			bike_map.drawcountries()
			bike_map.drawrivers()
			bike_map.fillcontinents(color='cornsilk', lake_color='lightblue')
			bike_map.drawmapboundary(fill_color='darkslategray')

			plt.title(str(temp_bucket) + ' Bucket')

			#Collisions
			bike_map.scatter(coords_by_temp[temp_bucket][1], coords_by_temp[temp_bucket][0], latlon=True, marker='o', color='firebrick', zorder=10, label='Collisions')
			#Brooklyn bridge entrance brooklyn side
			bike_map.scatter(-73.99, 40.7005, latlon=True, marker='o', color='deeppink', zorder=10, label='Brooklyn Bridge')
			#Williamsburg bridge entrance brooklyn side
			bike_map.scatter(-73.9688, 40.7123, latlon=True, marker='o', color='dodgerblue', zorder=10, label='Williamsburg Bridge')
			#Prospect park center
			bike_map.scatter(-73.9690, 40.6602, latlon=True, marker='o', color='green', zorder=10, label='Center of Prospect Park')


		except IndexError:
		#else:	
			print 'except'
			print temp_bucket
			bike_map = Basemap(projection='merc', lat_0=40.7, lon_0=-74.0, resolution = 'h', area_thresh = 0.1, \
			    llcrnrlon=-74.1, \
			    llcrnrlat=40.55, \
			    urcrnrlon=-73.9, \
			    urcrnrlat=40.85)

			bike_map.drawcoastlines()
			bike_map.drawcountries()
			bike_map.drawrivers()
			bike_map.fillcontinents(color='cornsilk', lake_color='lightblue')
			bike_map.drawmapboundary(fill_color='darkslategray')

			plt.title('0 Bucket')

			#Collisions
			bike_map.scatter(-73.9580032, 40.7108634, coords_by_temp[temp_bucket][0], latlon=True, marker='o', color='firebrick', zorder=10, label='Collisions')
			#Brooklyn bridge entrance brooklyn side
			bike_map.scatter(-73.99, 40.7005, latlon=True, marker='o', color='deeppink', zorder=10, label='Brooklyn Bridge')
			#Williamsburg bridge entrance brooklyn side
			bike_map.scatter(-73.9688, 40.7123, latlon=True, marker='o', color='dodgerblue', zorder=10, label='Williamsburg Bridge')
			#Prospect park center
			bike_map.scatter(-73.9690, 40.6602, latlon=True, marker='o', color='green', zorder=10, label='Center of Prospect Park')


	print 'plotted'
	plt.suptitle('Collisions Involving Cyclists in Brooklyn', fontsize=24)
	plt.savefig('combined.jpg')
	plt.clf()

plot_map()


