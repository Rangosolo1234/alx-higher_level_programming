-- Imports a database from table dump
-- Displays average temperature(Farenheight) by city temperature in descending order
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
