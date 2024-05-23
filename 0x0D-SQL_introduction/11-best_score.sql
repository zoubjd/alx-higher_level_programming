-- selects all the scores >= 10
SELECT s.score, s.name
FROM second_table s
WHERE s.score >= 10
ORDER BY score DESC;
