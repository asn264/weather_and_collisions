CREATE EXTERNAL TABLE collisions( 
	datetime timestamp, 
	borough string, 
	zip_code int, 
	latitude double, 
	longitude double, 
	location string, 
	on_street string, 
	cross_street string, 
	off_street string, 
	persons_injured int, 
	persons_killed int, 
	pedestrians_injured int, 
	pedestrians_killed int, 
	cyclist_injured int, 
	cyclist_killed int, 
	motorist_injured int, 
	motorist_killed int, 
	contributing_factor_vehicle_1 string, 
	contributing_factor_vehicle_2 string, 
	contributing_factor_vehicle_3 string, 
	contributing_factor_vehicle_4 string, 
	contributing_factor_vehicle_5 string, 
	unique_key int, 
	vehicle_type_code_1 string, 
	vehicle_type_code_2 string, 
	vehicle_type_code_3 string, 
	vehicle_type_code_4 string, 
	vehicle_type_code_5 string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://ass502-ds1004-project/input/vehicle_collisions/';