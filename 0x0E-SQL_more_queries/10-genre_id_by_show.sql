-- Dump from hbtn_0d_tvshows to your mySQL server
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
