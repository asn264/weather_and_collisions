--Accident counts by borough
SELECT borough, COUNT(*)
FROM weather_collisions
GROUP BY borough
ORDER BY borough;
