'''
Aditi Nair
May 2016

Comparing the distribution of temperature events and collisions.
'''

import matplotlib.pyplot as plt
import numpy as np


def temp_distribution():

	temp_buckets = []
	counts = []

	with open('temperature_distribution.tsv', 'rb') as temp_dist:
		
		for line in temp_dist:

			data = line.strip().split('\t')
			try:
				#Will raise ValueError for first row with data[0] = NULL
				temp_buckets.append(int(data[0]))
				counts.append(int(data[1]))
			except ValueError:
				pass

	tot = float(sum(counts))
	percents = [counts[i]*100/tot for i in range(len(counts))]

	return temp_buckets, percents


def temp_and_accident_frequency():

	temp_buckets = []
	accident_counts = []

	with open('temp_and_accident_frequency.tsv', 'rb') as temp_and_accident_dist:

		for line in temp_and_accident_dist:
			data = line.strip().split('\t')
			try:
				#Will raise ValueError for first row with data[0] = NULL
				temp_buckets.append(int(data[1]))
				accident_counts.append(int(data[0]))
			except ValueError:
				pass

	tot = float(sum(accident_counts))
	percents = [accident_counts[i]*100/tot for i in range(len(accident_counts))]

	return temp_buckets, percents


def temp_and_pedestrian_cyclist_accidents():

	temp_buckets = []
	ped_injured = []
	ped_killed = []
	cyclist_injured = []
	cyclist_killed = []

	with open('temp_and_pedestrian_cyclist_accidents.tsv', 'rb') as accidents_by_type:

		for line in accidents_by_type:

			#order: pedestrians injured, pedestrians killed, cyclist injured, cyclist killed, temperature bucket
			data = line.strip().split('\t')

			try:
				ped_injured.append(int(data[0]))
				ped_killed.append(int(data[1]))
				cyclist_injured.append(int(data[2]))
				cyclist_killed.append(int(data[3]))
				temp_buckets.append(int(data[4]))

			except ValueError:
				pass

	ped_injured_tot = float(sum(ped_injured))
	ped_killed_tot = float(sum(ped_killed))
	cyclist_injured_tot = float(sum(cyclist_injured))
	cyclist_killed_tot = float(sum(cyclist_killed))

	ped_injured_percents = [ped_injured[i]*100/ped_injured_tot for i in range(len(temp_buckets))]
	ped_killed_percents = [ped_killed[i]*100/ped_killed_tot for i in range(len(temp_buckets))]
	cyclist_injured_percents = [cyclist_injured[i]*100/cyclist_injured_tot for i in range(len(temp_buckets))]
	cyclist_killed_percents = [cyclist_killed[i]*100/cyclist_killed_tot for i in range(len(temp_buckets))]

	return ped_injured_percents, ped_killed_percents, cyclist_injured_percents, cyclist_killed_percents, temp_buckets



def plot_temp_and_collisions_by_type():

	ped_injured_percents, ped_killed_percents, cyclist_injured_percents, cyclist_killed_percents, temp_buckets = temp_and_pedestrian_cyclist_accidents()
	temp_percents = temp_distribution()[1]

	plt.title('Distribution of Temperature versus Distribution of Collisions by Type given Temperature')
	plt.plot(temp_buckets, ped_injured_percents, linestyle='--', marker='o', label='Pedestrians Injured')
	plt.plot(temp_buckets, ped_killed_percents, linestyle='--', marker='o', label='Pedestrians Killed')
	plt.plot(temp_buckets, cyclist_injured_percents, linestyle='--', marker='o', label='Cyclists Injured')
	plt.plot(temp_buckets, cyclist_killed_percents, linestyle='--', marker='o', label='Cyclists Killed')
	plt.plot(temp_buckets, temp_percents, linestyle='--', marker='o', label='Percent of Weather Events')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc=2)
	plt.savefig('temp_and_collisions_by_type.jpg')
	plt.clf()


def plot_temp_and_collisions_by_type_ratio():

	ped_injured_percents, ped_killed_percents, cyclist_injured_percents, cyclist_killed_percents, temp_buckets = temp_and_pedestrian_cyclist_accidents()
	temp_percents = temp_distribution()[1]

	ped_injured_ratios = [ped_injured_percents[i]/temp_percents[i] for i in range(len(temp_buckets))]
	ped_killed_ratios = [ped_killed_percents[i]/temp_percents[i] for i in range(len(temp_buckets))]
	cyclist_injured_ratios = [cyclist_injured_percents[i]/temp_percents[i] for i in range(len(temp_buckets))]
	cyclist_killed_ratios = [cyclist_killed_percents[i]/temp_percents[i] for i in range(len(temp_buckets))]

	plt.title('Ratio of Weather Events versus Collisions by Type given Temperature')
	plt.plot(temp_buckets, ped_injured_ratios, linestyle='dotted', marker='o', label='Pedestrian Injured Ratio')
	plt.plot(temp_buckets, ped_killed_ratios, linestyle='dotted', marker='o', label='Pedestrians Killed Ratio')
	plt.plot(temp_buckets, cyclist_injured_ratios, linestyle='dotted', marker='o', label='Cyclists Injured Ratio')
	plt.plot(temp_buckets, cyclist_killed_ratios, linestyle='dotted', marker='o', label='Cyclists Killed Ratio')

	plt.plot(temp_buckets, np.ones(len(temp_buckets)), label='Baseline')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc=2)
	plt.savefig('temp_and_collisions_by_type_ratio.jpg')
	plt.clf()


def plot_ratio():

	temp_buckets, temp_percents = temp_distribution()
	accident_percents = temp_and_accident_frequency()[1]

	ratios = [accident_percents[i]/temp_percents[i] for i in range(len(temp_buckets))]

	plt.title('Ratio of Weather Events versus Collisions given Temperature')
	plt.plot(temp_buckets, ratios, linestyle='dotted', marker='o', label='Ratio')
	plt.plot(temp_buckets, np.ones(len(temp_buckets)), label='Baseline')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc=2)
	plt.savefig('ratio.jpg')
	plt.clf()


def plot_temp_and_collisions():
	
	temp_buckets, temp_percents = temp_distribution()
	accident_percents = temp_and_accident_frequency()[1]

	plt.title('Distribution of Temperature versus Disribution of Collisions given Temperature')
	plt.plot(temp_buckets, temp_percents, linestyle='--', marker='o', label='Percent of Weather Events')
	plt.plot(temp_buckets, accident_percents, linestyle='--', marker='o', label='Percent of Accident Events')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc=2)
	plt.savefig('temp_and_collisions.jpg')
	plt.clf()


plot_temp_and_collisions()
plot_ratio()
plot_temp_and_collisions_by_type()
plot_temp_and_collisions_by_type_ratio()
