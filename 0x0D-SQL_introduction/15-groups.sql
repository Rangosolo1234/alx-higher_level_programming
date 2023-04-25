-- Groups items of a table with same values of score and prints them in decsending order
SELECT `score`, COUNT(score) AS number FROM `second_table` GROUP BY `score` ORDER BY `score` DESC;
