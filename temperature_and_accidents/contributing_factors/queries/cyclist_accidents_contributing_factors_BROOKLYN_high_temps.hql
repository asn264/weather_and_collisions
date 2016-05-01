SELECT contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5, COUNT(*) as x
FROM weather_collisions
WHERE (cyclist_injured > 0 or cyclist_killed > 0) AND borough='BROOKLYN' AND temp_farenheit >= 60
GROUP BY contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5
ORDER BY x DESC;
