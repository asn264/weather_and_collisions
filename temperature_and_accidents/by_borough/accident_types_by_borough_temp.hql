--Accident counts by borough by temperature bucket
SELECT borough, floor(temp_farenheit/10)*10 as bucket, SUM(pedestrians_injured), SUM(pedestrians_killed), SUM(cyclist_injured), SUM(cyclist_killed)
FROM weather_collisions
GROUP BY borough, bucket
ORDER BY borough, bucket;