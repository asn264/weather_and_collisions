SELECT FLOOR(gust/5)*5 as bucket,COUNT(*)
FROM weather
GROUP BY FLOOR(gust/5)*5
ORDER BY bucket;

