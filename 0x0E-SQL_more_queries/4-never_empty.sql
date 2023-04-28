-- Create table id_not_null
-- Attributes id INT with the default value 1, name VARCHAR(256)
-- If table exists should not fail
-- Cannot contail null value instead 1 by default
REATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
