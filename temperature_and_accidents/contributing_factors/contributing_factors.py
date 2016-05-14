'''
Aditi Nair
May 2016
Analyzing what contributing factors were cited in different kinds of accidents.
'''

from operator import itemgetter
import sys

def cyclist_accidents_contributing_factors():

	counts = {}
	sum = 0

	with open('cyclist_accidents_contributing_factors.tsv', 'rb') as doc:

		for line in doc:

			data = line.strip().split('\t')

			for i in range(len(data)-1):
				if data[i] in counts:
					counts[data[i]] += int(data[-1])
				else:
					counts[data[i]] = int(data[-1])
				sum += float(data[-1])

	for key in counts:
		counts[key] /= float(sum)

	sorted_count = sorted(counts.items(), key=itemgetter(1))
	print sorted_count


def cyclist_accidents_high_temperatures_contributing_factors():

	counts = {}
	sum = 0

	with open('cyclist_accidents_contributing_factors_high_temps.tsv', 'rb') as doc:

		i = 0
		for line in doc:

			data = line.strip().split('\t')

			for i in range(len(data)-1):
				if data[i] in counts:
					counts[data[i]] += int(data[-1])
				else:
					counts[data[i]] = int(data[-1])
				sum += float(data[-1])

	for key in counts:
		counts[key] /= float(sum)

	sorted_count = sorted(counts.items(), key=itemgetter(1))
	print sorted_count


def cyclist_accidents_BROOKLYN_contributing_factors():

	counts = {}
	sum = 0

	with open('cyclist_accidents_contributing_factors_BROOKLYN.tsv', 'rb') as doc:

		i = 0
		for line in doc:

			data = line.strip().split('\t')

			for i in range(len(data)-1):
				if data[i] in counts:
					counts[data[i]] += int(data[-1])
				else:
					counts[data[i]] = int(data[-1])
				sum += float(data[-1])

	for key in counts:
		counts[key] /= float(sum)

	sorted_count = sorted(counts.items(), key=itemgetter(1))
	print sorted_count


def cyclist_accidents_high_temperatures_BROOKLYN_contributing_factors():

	counts = {}
	sum = 0

	with open('cyclist_accidents_contributing_factors_BROOKLYN_high_temps.tsv', 'rb') as doc:

		i = 0
		for line in doc:

			data = line.strip().split('\t')

			for i in range(len(data)-1):
				if data[i] in counts:
					counts[data[i]] += int(data[-1])
				else:
					counts[data[i]] = int(data[-1])
				sum += float(data[-1])

	for key in counts:
		counts[key] /= float(sum)

	sorted_count = sorted(counts.items(), key=itemgetter(1))
	print sorted_count


def ped_injured_STATEN_ISLAND_contributing_factors():
	
	'''Only in cold weather'''

	counts = {}
	sum = 0

	with open('ped_injured_staten_island.tsv', 'rb') as doc:

		i = 0
		for line in doc:

			data = line.strip().split('\t')

			for i in range(len(data)-1):
				if data[i] in counts:
					counts[data[i]] += int(data[-1])
				else:
					counts[data[i]] = int(data[-1])
				sum += float(data[-1])

	for key in counts:
		counts[key] /= float(sum)

	sorted_count = sorted(counts.items(), key=itemgetter(1))
	print sorted_count

print 'cyclist accidents: '
cyclist_accidents_contributing_factors()
print '\n\ncyclist accidents high temperatures: '
cyclist_accidents_high_temperatures_contributing_factors()
print '\n\ncyclist accidents brooklyn: '
cyclist_accidents_BROOKLYN_contributing_factors()
print '\n\ncyclist accidents brooklyn high temperatures: '
cyclist_accidents_high_temperatures_BROOKLYN_contributing_factors()
print '\n\nped injured staten island: '
ped_injured_STATEN_ISLAND_contributing_factors()