--Take the cross-product of the two tables - don't limit by day or month, since you might throw out a 'nearest' relation
--Have a column that computes the difference between the weather timestamp and the collisions timestamp
--For each collision, only keep the row with the smallest absolute value difference


--Save as cross product table CP using SELECT * and then copying it to S3
SELECT *, ABS(unix_timestamp(weather.EST_time) - unix_timestamp(collisions.datetime)) as diff
FROM collisions
INNER JOIN weather
on (weather.USAF_station_num is not NULL);

--Now load the cross_prod table from csv


--Only keep values with smallest absolute value difference (ie min value of diff by collision)
SELECT * 
FROM cross_prod
INNER JOIN
(
	SELECT MIN(diff) as closest, datetime
	FROM cross_prod
	GROUP BY datetime
) AS temp
ON (temp.closest = cross_prod.diff) AND (temp.datetime = cross_prod.datetime);