SELECT floor(temp_farenheit/10)*10 as bucket,COUNT(*)
FROM weather
GROUP BY floor(temp_farenheit/10)*10
ORDER BY bucket;
