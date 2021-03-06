--This script loads the weather data from an S3 bucket into a Hive table called weather

CREATE EXTERNAL TABLE weather( 
	  USAF_station_num string, 
	  WBAN_station_num string,
	  EST_time timestamp,
	  wind_dir int,
	  wind_speed double,
	  gust double, 
	  cloud_ceiling int, 
	  sky_cover string, 
	  low_cloud_type string,
	  middle_cloud_type string,
	  high_cloud_type string,
	  visibility double,
	  manual_present_weather_1 int, 
	  manual_present_weather_2 int, 
	  manual_present_weather_3 int,
	  manual_present_weather_4 int,
	  auto_observed_present_weather_1 int, 
	  auto_observed_present_weather_2 int, 
	  auto_observed_present_weather_3 int,
	  auto_observed_present_weather_4 int, 
	  past_weather_indicator string, 
	  temp_farenheit int, 
	  dewpoint int,    
	  sea_level_pressure double,   
	  altimeter double,    
	  station_pressure double, 
	  max_temp_farenheit int, 
	  min_temp_farenheit int, 
	  liquid_precip_1_hr double, 
	  liquid_precip_6_hr double,
	  liquid_precip_24_hr double,
	  liquid_precip_xx_hr double,
	  snow_depth double)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://bigdata-weather-collisions-project/weather_data/';
