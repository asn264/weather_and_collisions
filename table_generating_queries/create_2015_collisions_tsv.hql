--This script selects the appropriate datetime range from the collisions table, the output can be saved as a tsv and is loaded into the 2015_collisions table

SELECT * FROM collisions WHERE datetime >= '2015-01-01 00:00:00' and datetime <= '2015-12-31 23:59:59';
