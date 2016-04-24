--Number of distinct columns
SELECT COUNT(DISTINCT 
USAF_station_num*100/ct, 
WBAN_station_num*100/ct,
EST_time*100/ct,
wind_dir*100/ct,
wind_speed*100/ct,
gust*100/ct, 
cloud_ceiling*100/ct, 
sky_cover*100/ct, 
low_cloud_type*100/ct,
middle_cloud_type*100/ct,
high_cloud_type*100/ct,
visibility*100/ct,
manual_present_weather_1*100/ct, 
manual_present_weather_2*100/ct, 
manual_present_weather_3*100/ct,
manual_present_weather_4*100/ct,
auto_observed_present_weather_1*100/ct, 
auto_observed_present_weather_2*100/ct, 
auto_observed_present_weather_3*100/ct,
auto_observed_present_weather_4*100/ct, 
past_weather_indicator*100/ct, 
temp_farenheit*100/ct, 
dewpoint*100/ct,
sea_level_pressure*100/ct,   
altimeter*100/ct,    
station_pressure*100/ct, 
max_temp_farenheit*100/ct, 
min_temp_farenheit*100/ct, 
liquid_precip_1_hr*100/ct, 
liquid_precip_6_hr*100/ct,
liquid_precip_24_hr*100/ct,
liquid_precip_xx_hr*100/ct,
snow_depth*100/ct)
FROM weather
INNER JOIN
(
	SELECT COUNT(*) as ct
	FROM WEATHER
) tot
ON (tot.ct > 1)
GROUP BY ct;
