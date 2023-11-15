-- sorted by ascending genre name.
SELECT DISTINCT name FROM tv_genres AS k
INNER JOIN tv_show_genres AS i
ON k.id = i.genre_id
INNER JOIN tv_shows AS s
ON i.show_id = s.id
WHERE k.name NOT IN
(SELECT name FROM tv_genres AS k
INNER JOIN tv_show_genres AS i
ON k.id = i.genre_id
INNER JOIN tv_shows AS s
ON i.show_id = s.id
WHERE s.title = "Dexter")
ORDER BY k.name;
