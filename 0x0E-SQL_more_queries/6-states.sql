-- Creates database named hbtn_0d_usa
-- Creates table named states in the database
-- States containsa attributes:
-- id INT unique, auto generated, can’t be null and is a primary key
-- and name VARCHAR(256) can’t be null
-- If database or table exists code should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
