SELECT FLOOR(wind_speed/5)*5, COUNT(*) 
FROM weather_collisions 
GROUP BY FLOOR(wind_speed/5)*5;
