'''
Author: Akash Shah
Converts date and time stamp into a datetime column that works with Hive.
Also, removes '\n' that were inserted in the middle of a row and resulted in malformed data.
'''

import sys
import csv

temp_line = None

with open('../data/NYPD_Motor_Vehicle_Collisions.csv','r') as f:
	with open('../data/clean_NYPD_Motor_Vehicle_Collisions.csv','w') as out_f:
		
		count = 0
		for line in f:
			#for the first line, combine the date and time columns to a single datetime column and count the number of fields
			if count == 0:
				date,time,other_data = line.split(',',2)
				out_f.write('DATETIME,'+other_data.strip('\n')+',ID\n')
				count += 1

				actual_field_counts = line.count(',') + 1
			else:
				#if the line is malformed by having less fields that normal
				if line.count(',') + 1 < actual_field_counts:
					#if this is the first malformed line, store the data
					if temp_line is None:
						
						temp_line = line
					#if this is the next malformed line, combine it with the previous one to form a proper new line
					else:
						new_line = temp_line.strip('\n')+line

						date,time,other_data = new_line.split(',',2)
						
						month,day,year = date.split('/',2)

						#if the hour is a single digit, make it double digit ie 5 -> 05
						if len(time.split(':')[0]) == 1:
							time = '0'+time
						time = time+':00'

						out_f.write(year+'-'+month+'-'+day+' '+time+','+other_data.strip('\n')+','+str(count)+'\n')
						count += 1

						temp_line = None
				#for data, format the date and time into a single column and add seconds		
				else:
					date,time,other_data = line.split(',',2)

					month,day,year = date.split('/',2)

					#if the hour is a single digit, make it double digit ie 5 -> 05
					if len(time.split(':')[0]) == 1:
						time = '0'+time
					time = time+':00'

					out_f.write(year+'-'+month+'-'+day+' '+time+','+other_data.strip('\n')+','+str(count)+'\n')
					count += 1

field_counts = {}
with open('../data/clean_NYPD_Motor_Vehicle_Collisions.csv','r') as f:
	with open('../data/clean_NYPD_Motor_Vehicle_Collisions.tsv','w') as out_f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		writer = csv.writer(out_f, delimiter='\t')
		for row in reader:
			writer.writerow(row)
			field_counts[len(row)] = field_counts.get(len(row),0)+1
