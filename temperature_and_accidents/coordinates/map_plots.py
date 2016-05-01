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
	
	return coords_by_temp


def plot_map():

	coords_by_temp = load_data()

	for temp_bucket in coords_by_temp:

		try:
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

			plt.title('Collisions Involving Cyclists in ~' + str(temp_bucket) + ' Degree Weather')

			#Collisions
			bike_map.scatter(coords_by_temp[temp_bucket][1], coords_by_temp[temp_bucket][0], latlon=True, marker='o', color='firebrick', zorder=10, label='Collisions')
			#Brooklyn bridge entrance brooklyn side
			bike_map.scatter(-73.99, 40.7005, latlon=True, marker='o', color='deeppink', zorder=10, label='Brooklyn Bridge')
			#Williamsburg bridge entrance brooklyn side
			bike_map.scatter(-73.9688, 40.7123, latlon=True, marker='o', color='dodgerblue', zorder=10, label='Williamsburg Bridge')
			#Prospect park center
			bike_map.scatter(-73.9690, 40.6602, latlon=True, marker='o', color='green', zorder=10, label='Center of Prospect Park')
			plt.legend(loc='upper left', prop={'size':7})
			plt.savefig('map_'+str(temp_bucket)+'.jpg')
			plt.clf()

		except IndexError:
			
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

			plt.title('Collisions Involving Cyclists in ~0 Degree Weather')

			#Collisions
			bike_map.scatter(-73.9580032, 40.7108634, coords_by_temp[temp_bucket][0], latlon=True, marker='o', color='firebrick', zorder=10, label='Collisions')
			#Brooklyn bridge entrance brooklyn side
			bike_map.scatter(-73.99, 40.7005, latlon=True, marker='o', color='deeppink', zorder=10, label='Brooklyn Bridge')
			#Williamsburg bridge entrance brooklyn side
			bike_map.scatter(-73.9688, 40.7123, latlon=True, marker='o', color='dodgerblue', zorder=10, label='Williamsburg Bridge')
			#Prospect park center
			bike_map.scatter(-73.9690, 40.6602, latlon=True, marker='o', color='green', zorder=10, label='Center of Prospect Park')
			plt.legend(loc='upper left', prop={'size':7})
			plt.savefig('map_0.jpg')
			plt.clf()

	print 'plotted'

plot_map()


