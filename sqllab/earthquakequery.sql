
-- Shows the top 15 places with the highest amount of earthquakes
SELECT place, COUNT(*) AS num_earthquakes
FROM earthquakes
GROUP BY place
ORDER BY num_earthquakes DESC
LIMIT 15;

--Displays the top ten earthquakes with the highest magnitued
SELECT *
FROM earthquakes
ORDER BY magError DESC
LIMIT 10;

--Averages the magnitude of the earthquakes from each loaction source
SELECT locationSource, AVG(mag) AS avg_magnitude
FROM earthquakes
GROUP BY locationSource
ORDER BY avg_magnitude DESC;



