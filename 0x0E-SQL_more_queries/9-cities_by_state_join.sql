-- Lists all cities contained in hbtn_0d_usa database
-- Each record should display: cities.id - cities.name - states.name
-- Results are be sorted in ascending order by cities.id
-- Joins cities to the states they belong

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
