SELECT COUNT(*), visibility 
FROM weather_collisions
GROUP BY visibility
ORDER BY visibility;
