SELECT d.model, s.aircraft_code, COUNT(s.aircraft_code) AS seats_count
FROM aircrafts_data d LEFT JOIN seats s ON d.aircraft_code=s.aircraft_code
GROUP BY d.model, s.aircraft_code
ORDER BY seats_count desc
LIMIT 1;