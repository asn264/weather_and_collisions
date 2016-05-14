SELECT contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5,COUNT(*) as x
FROM weather_collisions
WHERE cyclist_injured = 0 and cyclist_killed = 0 and pedestrians_injured=0 and pedestrians_killed=0 and vehicle_type_code_1 <> 'BICYCLE' and vehicle_type_code_2 <> 'BICYCLE' and temp_farenheit < 30
GROUP BY contributing_factor_vehicle_1,contributing_factor_vehicle_2,contributing_factor_vehicle_3,contributing_factor_vehicle_4,contributing_factor_vehicle_5
ORDER BY x DESC;
