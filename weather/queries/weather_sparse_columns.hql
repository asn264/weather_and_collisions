--Count what percent of each column is NULL - useful to figure out what fields are most consistently informative
SELECT COUNT(USAF_station_num)*100/tot, COUNT(WBAN_station_num)*100/tot, COUNT(EST_time)*100/tot, COUNT(wind_dir)*100/tot, COUNT(wind_speed)*100/tot, COUNT(gust)*100/tot, 
COUNT(cloud_ceiling)*100/tot, COUNT(sky_cover)*100/tot, COUNT(low_cloud_type)*100/tot, COUNT(middle_cloud_type)*100/tot, COUNT(high_cloud_type)*100/tot, COUNT(visibility)*100/tot,
COUNT(manual_present_weather_1)*100/tot, COUNT(manual_present_weather_2)*100/tot, COUNT(manual_present_weather_3)*100/tot, COUNT(manual_present_weather_4)*100/tot,
COUNT(auto_observed_present_weather_1)*100/tot, COUNT(auto_observed_present_weather_2)*100/tot, COUNT(auto_observed_present_weather_3)*100/tot, COUNT(auto_observed_present_weather_4)*100/tot, COUNT(past_weather_indicator)*100/tot, COUNT(temp_farenheit)*100/tot, COUNT(dewpoint)*100/tot, COUNT(sea_level_pressure)*100/tot, 
COUNT(altimeter)*100/tot, COUNT(station_pressure)*100/tot, COUNT(max_temp_farenheit)*100/tot, COUNT(min_temp_farenheit)*100/tot, COUNT(liquid_precip_1_hr)*100/tot, 
COUNT(liquid_precip_6_hr)*100/tot, COUNT(liquid_precip_24_hr)*100/tot, COUNT(liquid_precip_xx_hr)*100/tot, COUNT(snow_depth)*100/tot
FROM weather
INNER JOIN
(
	SELECT COUNT(*) as tot
	FROM weather
) table
ON (table.tot>0)
GROUP BY tot;
