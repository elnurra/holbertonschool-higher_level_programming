-- Subquery to get genre_ids linked to the show "Dexter"
-- Subquery to get the id of the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY tv_genres.name ASC;

