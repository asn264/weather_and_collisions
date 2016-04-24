import csv

with open('../data/clean_NYPD_Motor_Vehicle_Collisions.csv','rb') as csvfile:
	col_reader = csv.reader(csvfile,delimiter=',')
	num_fields = {}
	for row in col_reader:
		num_fields[len(row)]=num_fields.get(len(row),0)+1

print num_fields