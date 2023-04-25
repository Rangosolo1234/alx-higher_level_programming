-- Lists all rows of a table except those without name values
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
