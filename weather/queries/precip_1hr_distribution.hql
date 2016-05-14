SELECT liquid_precip_1_hr,COUNT(*)
FROM weather
GROUP BY liquid_precip_1_hr;
