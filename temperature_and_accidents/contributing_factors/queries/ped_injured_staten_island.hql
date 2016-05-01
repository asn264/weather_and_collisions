SELECT contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5, COUNT(*) as x
FROM weather_collisions
WHERE pedestrians_injured > 0 AND temp_farenheit <= 30 AND borough='STATEN ISLAND'
GROUP BY contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5
ORDER BY x DESC;