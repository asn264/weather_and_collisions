SELECT FLOOR(wind_speed/5)*5 as bucket,COUNT(*)
FROM weather
GROUP BY FLOOR(wind_speed/5)*5
ORDER BY bucket;
