SELECT visibility,COUNT(*) 
FROM weather
GROUP BY visibility
ORDER BY visibility;
