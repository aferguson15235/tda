SET SQL_SAFE_UPDATES = 0;

-- selecting all the records in the surveys table
SELECT * FROM survey_new;

-- select the year, month, day from the surveys table
SELECT year, month, day FROM survey_new;

/* this is a double line comment
sql engine will ignore it */

-- limit the record to the first 10 
SELECT * FROM survey_new 
LIMIT 10;

-- select unique records
SELECT DISTINCT species_id
FROM survey_new;

-- calculated values
SELECT species_id, weight * 1000 as weight_mg
FROM survey_new;

-- rounding values
SELECT year, month, day, species_id, ROUND(weight/1000,2) as weight_kg
FROM survey_new; 

-- filtering expressions
SELECT *
FROM survey_new
WHERE species_id='DM';

SELECT * FROM survey_new
WHERE year <= 2000;

SELECT year, species_id, weight/1000 as weight_kg FROM survey_new
WHERE (plot_id = 1) or (weight >= 75);

SELECT *
FROM survey_new
WHERE species_id='DM' or species_id = 'DO' or species_id = 'DS';

SELECT *
FROM survey_new
WHERE weight <=75 and species_id in ('DM', 'DO', 'DS');

-- sorting output
SELECT * FROM species
ORDER BY genus DESC, species;

-- challenge
SELECT year, species_id, weight/1000 as weight_kg FROM survey_new
ORDER BY weight DESC;

-- count number of rows in table
SELECT COUNT(*) as surveys_count, MAX(weight), MIN(weight), AVG(weight)
FROM survey_new;

-- group by
SELECT species_id, COUNT(*) as surveys_count
FROM survey_new
GROUP BY species_id;

-- challenge
SELECT species_id, year, count(*) as year_count, avg(weight) as year_average
FROM survey_new
GROUP BY species_id, year
ORDER BY species_id, year;

-- species ordered by number captured
SELECT species_id, count(*) as species_count
FROM survey_new
GROUP BY species_id
ORDER BY count(*) DESC;

-- number of species in each taxa with at least 10 species
SELECT taxa, count(species) as number_of_species
FROM species
GROUP BY taxa
HAVING count(species_id) > 10;

-- creating samples from large databases
CREATE VIEW summer_2000 AS
SELECT *
FROM survey_new
WHERE year = 2000 and (month > 4 and month < 10);

SELECT *
FROM summer_2000;

-- task
CREATE VIEW before_2000 AS
SELECT *
FROM survey_new
WHERE year < 2000;

SELECT *
FROM before_2000
WHERE sex = 'M';

SELECT count(*) as count_by_sex
FROM before_2000
WHERE sex = 'M' or sex IS NULL;
