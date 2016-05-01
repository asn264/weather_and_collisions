import matplotlib.pyplot as plt
import numpy as np

'''

'''

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



def accidents_by_borough():

	boroughs = []
	counts = []

	with open('accidents_by_borough.tsv', 'rb') as accidents_by_borough:
		
		for line in accidents_by_borough:
			
			data = line.strip().split('\t')

			if len(data)>1:
				boroughs.append(data[0])
				counts.append(int(data[1]))

	return boroughs, counts


def accidents_by_type_by_borough():

	boroughs = []
	breakdown = []

	with open('accident_types_by_borough.tsv', 'rb') as accident_types_by_borough:

		for line in accident_types_by_borough:

			data = line.strip().split('\t')

			if len(data) > 4:
				boroughs.append(data[0])
				breakdown.append([int(data[1]), int(data[2]), int(data[3]), int(data[4])])

	return boroughs, breakdown


def accidents_by_borough_temp():

	'''By borough, how many accidents happen in each temperature bucket'''

	info = {}

	with open('accidents_by_borough_temp.tsv', 'rb') as accidents_by_borough_temp:

		for line in accidents_by_borough_temp:

			data = line.strip().split('\t')

			if len(data) > 2 and data[1] != 'NULL':
				if data[0] in info:
					info[data[0]][0].append(int(data[1]))
					info[data[0]][1].append(int(data[2]))
				else:
					info[data[0]] =[[int(data[1])],[int(data[2])]]

	return info


def accident_types_by_borough_temp():

	info = {}

	with open('accident_types_by_borough_temp.tsv') as doc:

		for line in doc:

			data = line.strip().split('\t')

			if len(data) > 5 and data[1] != 'NULL':

				if data[0] in info:
					info[data[0]][0].append(int(data[1]))
					info[data[0]][1].append(int(data[2]))
					info[data[0]][2].append(int(data[3]))
					info[data[0]][3].append(int(data[4]))
					info[data[0]][4].append(int(data[5]))

				else:
					info[data[0]] = [ [int(data[1])], [int(data[2])], [int(data[3])], [int(data[4])], [int(data[5])] ]

	return info


def plot_accidents_by_temp_by_borough():

	buckets, baseline_percents = temp_distribution()

	#dictionary: each key is a borough. value is list of lists. second list is the count of accidents. follows bucket ordering.
	by_borough_info = accidents_by_borough_temp()

	for borough in by_borough_info:

		c_borough_counts = by_borough_info[borough][1]
		c_tot = sum(c_borough_counts)
		c_borough_percents = [c_borough_counts[i]*100/c_tot for i in range(len(c_borough_counts))]
		plt.plot(buckets, c_borough_percents, linestyle='--', marker='o', label='% Collisions: ' + borough)

	plt.plot(buckets, baseline_percents, linestyle='--', marker='o', label='% Weather')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc='upper left', prop={'size':9})
	plt.show()



def plot_accidents_by_temp_by_borough_ratio():

	buckets, baseline_percents = temp_distribution()

	#dictionary: each key is a borough. value is list of lists. second list is the count of accidents. follows bucket ordering.
	by_borough_info = accidents_by_borough_temp()

	for borough in by_borough_info:

		c_borough_counts = by_borough_info[borough][1]
		c_tot = sum(c_borough_counts)
		c_borough_percents = [c_borough_counts[i]*100/c_tot for i in range(len(c_borough_counts))]

		ratios = [c_borough_percents[i]/baseline_percents[i] for i in range(len(c_borough_percents))]
		plt.title('Ratio of Collision Events to Weather Events: ' + borough)
		plt.plot(buckets, ratios, linestyle='--', marker='o', label=borough)

	plt.plot(buckets, np.ones(len(ratios)), label='Baseline')
	plt.xlabel('Degrees Farenheit')
	plt.legend(loc='upper left', prop={'size':9})
	plt.title('Ratio of Collisions Percents to Weather Occurence Percents')
	plt.show()	


def plot_accidents_by_temp_by_type_by_borough_ratio():

	'''In each borough, what percent of accidents are pedestrian injured, pedestrian killed, etc.'''

	buckets, baseline_percents = temp_distribution()

	#dictionary: each key is a borough. value is a list of lists. list 1,2,3,4 are pedestrians_injured, pedestrians_killed, cyclist_injured, cylist_killed
	by_borough_info = accident_types_by_borough_temp()

	for borough in by_borough_info:

		pedestrians_injured_counts = by_borough_info[borough][1] 
		pedestrians_killed_counts = by_borough_info[borough][2]
		cyclist_injured_counts = by_borough_info[borough][3]
		cyclist_killed_counts = by_borough_info[borough][4]

		pedestrians_injured_tot = sum(pedestrians_injured_counts)
		pedestrians_injured_percents = [pedestrians_injured_counts[i]*100/pedestrians_injured_tot for i in range(len(pedestrians_injured_counts))]

		pedestrians_killed_tot = sum(pedestrians_killed_counts)
		pedestrians_killed_percents = [pedestrians_killed_counts[i]*100/pedestrians_killed_tot for i in range(len(pedestrians_killed_counts))]

		cyclist_injured_tot = sum(cyclist_injured_counts)
		cyclist_injured_percents = [cyclist_injured_counts[i]*100/cyclist_injured_tot for i in range(len(cyclist_injured_counts))]

		cyclist_killed_tot = sum(cyclist_killed_counts)
		cyclist_killed_percents = [cyclist_killed_counts[i]*100/cyclist_killed_tot for i in range(len(cyclist_killed_counts))]

		predestrians_injured_ratios = [pedestrians_injured_percents[i]/baseline_percents[i] for i in range(len(pedestrians_injured_percents))]
		predestrians_killed_ratios = [pedestrians_killed_percents[i]/baseline_percents[i] for i in range(len(pedestrians_killed_percents))]
		cyclist_injured_ratios = [cyclist_injured_percents[i]/baseline_percents[i] for i in range(len(cyclist_injured_percents))] 
		cyclist_killed_ratios = [cyclist_killed_percents[i]/baseline_percents[i] for i in range(len(cyclist_killed_percents))] 
		
		plt.title(borough)
		plt.plot(buckets, predestrians_injured_ratios, linestyle='--', marker='o', label='Ped Injured')
		plt.plot(buckets, predestrians_killed_ratios, linestyle='--', marker='o', label='Ped Killed')
		plt.plot(buckets, cyclist_injured_ratios, linestyle='--', marker='o', label='Cyclist Injured')
		plt.plot(buckets, cyclist_killed_ratios, linestyle='--', marker='o', label='Cyclist Killed')
		plt.plot(buckets, np.ones(len(buckets)), label='Baseline')
	
		plt.legend(loc='upper left', prop={'size':9})
		plt.savefig('accidents_by_type_by_temp_'+borough+'.pdf')
		plt.clf()

plot_accidents_by_temp_by_borough()
plot_accidents_by_temp_by_borough_ratio()
plot_accidents_by_temp_by_type_by_borough_ratio()



