-- lists all records of the table 
SELECT s.score, s.name
FROM second_table s
WHERE s.name IS NOT NULL AND s.name != ''
ORDER BY s.score DESC;
