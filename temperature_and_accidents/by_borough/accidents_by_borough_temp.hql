--Accident counts by borough by temperature bucket
SELECT borough, floor(temp_farenheit/10)*10 as bucket, COUNT(*)
FROM weather_collisions
GROUP BY borough, bucket
ORDER BY borough, bucket;