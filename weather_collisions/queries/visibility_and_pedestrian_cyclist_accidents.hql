SELECT SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed), visibility
FROM weather_collisions
GROUP BY visibility
ORDER BY visibility; 
