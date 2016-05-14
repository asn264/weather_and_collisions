'''Author: Akash Shah

This script analyzes the contributing factors for motor-on-motor collisions in various temperature conditions, as well as generally'''

from operator import itemgetter
import sys


def motor_collisions_factors():
	'''contributing factors for motor collisions, regardless of weather'''

	counts = {}
	sum = 0

	with open('output/motor_collisions_factors.tsv', 'rb') as doc:

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

	sorted_count = sorted(counts.items(), key=itemgetter(1),reverse=True)
	print sorted_count[:10]


def motor_collisions_factors_high_temp():
	'''contributing factors for motor collisions during high temperatures'''

	counts = {}
	sum = 0

	with open('output/motor_collisions_factors_high_temp.tsv', 'rb') as doc:

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

	sorted_count = sorted(counts.items(), key=itemgetter(1),reverse=True)
	print sorted_count[:10]


def motor_collisions_factors_low_temp():
	'''contributing factors for motor collisions during low temperatures'''

	counts = {}
	sum = 0

	with open('output/motor_collisions_factors_low_temp.tsv', 'rb') as doc:

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

	sorted_count = sorted(counts.items(), key=itemgetter(1),reverse=True)
	print sorted_count[:10]

motor_collisions_factors()
motor_collisions_factors_high_temp()
motor_collisions_factors_low_temp()

