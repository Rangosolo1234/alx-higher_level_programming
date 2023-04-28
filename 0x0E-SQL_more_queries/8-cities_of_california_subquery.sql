-- Lists all cities of California state in hbtn_0d_usa datyabse
-- This is a subquery
-- Results will be sorted according to cities id attribute

SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
