# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp, userid int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (userId int PRIMARY KEY, firstname varchar, lastname varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration float)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, artist_name varchar, artist_location varchar, artist_longitude varchar, artist_latitude varchar)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (start_time, userId, level, song_id, artist_id, session_id, location, user_agent) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s) \
                 ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""INSERT INTO users (userId, firstname, lastname, gender, level) \
                    VALUES (%s, %s, %s, %s, %s)\
                    ON CONFLICT (userId) DO NOTHING
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year,duration)\
                 VALUES (%s, %s, %s, %s, %s)\
                 ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists (artist_id,artist_name,artist_location, artist_longitude, artist_latitude) \
                 VALUES (%s, %s, %s, %s, %s) \
                 ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s)
                 ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""select songs.song_id, songs.artist_id from songs JOIN artists on songs.title = %s AND artists.artist_name = &s AND songs.duration = %s
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]