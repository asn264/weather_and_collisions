SELECT SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed), floor(temp_farenheit/10)*10 as bucket
FROM weather_collisions
GROUP BY floor(temp_farenheit/10)*10
ORDER BY bucket; 
