SET SQL_SAFE_UPDATES = 0;

-- creating a new database;
CREATE DATABASE andrew_db;

-- create a table
CREATE TABLE people(
person_id int,
last_name varchar(255),
first_name varchar(255),
job_title varchar(255),
report_to varchar(255)
);

-- add data to a table with some of the columns
INSERT INTO people (person_id, last_name, first_name, job_title)
VALUES  (1, 'Gru', 'Felonius', 'Super Villain');

-- add data to a table with all of the columns
INSERT INTO people 
VALUES  (2, 'Nefario', 'Doctor', 'Super Villain', 'Gru');

-- remove data from the table
DELETE FROM people
WHERE report_to = 'Gru';

-- add multiple rows to the table
INSERT INTO people
VALUES
	(3, NULL, 'Mel', 'Minion', 'Gru'),
    (4, NULL, 'Bob', 'Minion', 'Mel'),
    (5, NULL, 'Stewart', 'Minion', 'Mel'),
    (6, NULL, 'Kevin', 'Minion', 'Mel')
;

-- update data in a table
UPDATE people
SET job_title = 'Sidekick'
WHERE person_id = 2;

UPDATE people
set report_to = 'Nefario'
WHERE job_title = 'Minion';

-- remove column from table
ALTER TABLE people
DROP COLUMN first_name;

select * from people;