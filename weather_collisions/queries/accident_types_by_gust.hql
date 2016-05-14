SELECT FLOOR(gust/5)*5, SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed), SUM(motorist_injured), SUM(motorist_killed) 
FROM weather_collisions 
GROUP BY FLOOR(gust/5)*5;
