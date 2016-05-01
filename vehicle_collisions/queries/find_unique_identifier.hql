select max(num)
from
(
select datetime,location,unique_key,latitude,longitude,zip_code,vehicle_type_code_1,count(*) as num from collisions_2015 group by datetime,location,unique_key,latitude,longitude,zip_code,vehicle_type_code_1
) as t;