--This table assumes that the weather and collisions_2015 tables have already been generated, the output of this query can be saved as a tsv file

--Join collisions with all weather records on the same day, and then with all weather records on the previous day. Then take the union
CREATE TABLE partial_cross_prod AS
        SELECT *, unix_timestamp(collisions_2015.datetime) - unix_timestamp(weather.EST_time) as diff
        FROM collisions_2015
        INNER JOIN weather
        ON (to_date(weather.EST_time) = to_date(collisions_2015.datetime))
        UNION ALL
        SELECT *, unix_timestamp(collisions_2015.datetime) - unix_timestamp(weather.EST_time) as diff
        FROM collisions_2015
        INNER JOIN weather
        ON (DATE_ADD(to_date(weather.EST_time),1)=to_date(collisions_2015.datetime));


--Keep only values with the smallest absolute value difference
CREATE TABLE IF NOT EXISTS weather_collisions AS
SELECT *
FROM partial_cross_prod
INNER JOIN
(
        SELECT MIN(diff) as closest,id as temp_id
        FROM partial_cross_prod
        WHERE diff >= 0
        GROUP BY id
) AS temp
ON (temp.closest = partial_cross_prod.diff) AND (partial_cross_prod.id = temp.temp_id);