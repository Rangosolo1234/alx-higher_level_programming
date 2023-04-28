-- Imports databse of hbtn_0d_tvshows to your MySQL server
-- lists all shows contained in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order basing on tv_shows.title and
-- tv_show_genres.genre_id
-- Displays null if show doesn't have a genre

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
