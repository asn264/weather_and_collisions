SELECT latitude, longitude, FLOOR(temp_farenheit/10)*10
FROM weather_collisions
WHERE (cyclist_killed > 0 OR cyclist_injured > 0) AND borough = 'BROOKLYN';
