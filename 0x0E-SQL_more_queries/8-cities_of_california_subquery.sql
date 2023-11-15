-- cities of california
SELECT * FROM hbtn_0d_usa.cities
WHERE state_id IN (SELECT id FROM states WHERE name = California)
ORDER BY cities.id;
