SELECT cloud_ceiling,SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed)
FROM weather_collisions
GROUP BY cloud_ceiling; 

