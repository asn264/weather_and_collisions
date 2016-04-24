SELECT COUNT(*) FROM collisions_2015 WHERE unique_key IS NOT NULL;

SELECT COUNT(DISTINCT unique_key) FROM collisions_2015 WHERE unique_key IS NOT NULL;
