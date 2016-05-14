SELECT FLOOR(gust/5)*5, COUNT(*) 
FROM weather_collisions 
GROUP BY FLOOR(gust/5)*5;
