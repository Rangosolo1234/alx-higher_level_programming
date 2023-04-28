-- Creates table named unique_id
-- Table has attributes id INT, name VARCHAR(256)
-- With the default value 1 and must be unique for id
-- If table exists code should not fail

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
