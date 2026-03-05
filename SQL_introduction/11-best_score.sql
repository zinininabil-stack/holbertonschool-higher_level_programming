-- Script that lists all records with a score >= 10 in the table second_table of the database -- 
SELECT score, name FROM second_table ORDER BY score >= 10 DESC;