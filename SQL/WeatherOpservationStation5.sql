-- Print the longest and shortest name of the city from database

SELECT s.City, length(s.City) FROM STATION s ORDER BY length(City), City LIMIT 1;
SELECT s.City, length(s.City) FROM STATION s ORDER BY length(City) DESC, City LIMIT 1;