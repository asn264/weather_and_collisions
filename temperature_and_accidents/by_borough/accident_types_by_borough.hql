--Accident counts by type by borough
SELECT borough, SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed)
FROM weather_collisions
GROUP BY borough
ORDER BY borough;