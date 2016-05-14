SELECT floor(temp_farenheit/10)*10,COUNT(DISTINCT to_date(datetime))
FROM full_weather_collisions
GROUP BY floor(temp_farenheit/10)*10;

