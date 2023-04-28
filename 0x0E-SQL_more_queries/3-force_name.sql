-- Creates table named force_name
-- Has attributes id (INT) and name VARCHAR(256)
-- If table already exists code should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
