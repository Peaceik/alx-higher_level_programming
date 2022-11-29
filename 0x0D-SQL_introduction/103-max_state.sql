-- Display max temperature
-- Query to display max temp
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
