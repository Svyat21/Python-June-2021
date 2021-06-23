CREATE extension cube;
CREATE extension earthdistance;
SELECT c1.city, c2.city, (point(c1.coordinates) <@> point(c2.coordinates)) AS dist
FROM airports_data c1, airports_data c2
ORDER BY dist DESC
LIMIT 1;