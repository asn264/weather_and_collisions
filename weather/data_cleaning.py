'''
Aditi Nair

Quick script to transfer weather_data.txt to a csv with consistent delimiters, and update date information:
Hive datetime format, adjusted to EST according to daylight savings in 2015. 
'''

import csv

field_counts = {}

#Last day of each month. Index + 1 corresponds to month
last_day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('../data/weather-data.txt', 'rb') as in_data:
	with open('../data/clean_weather_data.csv', 'wb') as out_data:

		writer = csv.writer(out_data)

		for line in in_data:

			#Don't write the first line of column names to csv because Hive does not have a neat 'skip row' functionality
			if line[:6].strip() != 'USAF':

				#Sometimes 'T' appears instead of the delimiter ' ' in later field entries - detect and replace these
				if 'T' in line[46:]:
					data = (line[:46] + line[46:].replace('T',' ')).strip().split()
				else:
					data = line.strip().split()

				#Change date to Hive datetime format, accounting for Daylight Savings. 
				datetime = data[2]
				year = int(datetime[:4])
				month = int(datetime[4:6])
				day = int(datetime[6:8])
				hour = int(datetime[8:10])
				minutes = int(datetime[10:])

				#If before March 8th 2:00 AM or after November 1st 2:00 AM, subtract 5 from the hour:
				if (month < 3) or (month > 11) or \
					(month == 3 and day < 8) or (month == 11 and day > 1) or \
					(month == 3 and day == 8 and hour <= 2) or \
					(month == 11 and day == 1 and hour >= 2):
						hour -= 5

				#if between March 8th 2:00 AM and November 1st 2:00 AM, subtract 4:
				else:
					hour -= 4

				#Now a little arithmetic to make sure all the numbers still make sense:
				if hour < 0:
					day -= 1
					hour = 24 + hour
					if day == 0:
						if month > 1:
							month -= 1
							day = last_day_of_month[month-1]
						#At this point, you've rolled back to the previous year
						else:
							year = 2014

				#Write new date column, if year is still 2015: YYYY-MM-DD HH:MM:SS
				if year == 2015:
					new_datetime = str(year) + '-' + '{0:02d}'.format(month) + '-' + '{0:02d}'.format(day) + ' ' + '{0:02d}'.format(hour) + ':' + '{0:02d}'.format(minutes) + ':00'

					#Write corrected data to csv
					new_data = data[:2]+[new_datetime]+data[3:]
					writer.writerow(new_data)

					#Error-checking: dictionary should only have one key at the end
					if len(new_data) in field_counts:
						field_counts[len(new_data)] += 1
					else:
						field_counts[len(new_data)] = 1

print field_counts