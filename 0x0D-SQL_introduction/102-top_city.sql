-- Imports temperatures data to database
-- Displays only top three leading cities in months July and August
-- Order the three cities by temperature in descending order
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
