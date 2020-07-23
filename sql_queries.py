# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
      id SERIAL PRIMARY KEY,
      start_time TIMESTAMP,
      user_id INT,
      level VARCHAR,
      song_id VARCHAR,
      artist_id VARCHAR,
      session_id INT,
      location VARCHAR,
      user_agent VARCHAR
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
      id INT PRIMARY KEY,
      first_name VARCHAR,
      last_name VARCHAR,
      gender CHAR(1),
      level VARCHAR
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
      id VARCHAR PRIMARY KEY,
      title VARCHAR,
      artist_id VARCHAR,
      year INT,
      duration NUMERIC (20, 5)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
      id VARCHAR PRIMARY KEY,
      name VARCHAR,
      location VARCHAR,
      latitude NUMERIC (8, 5),
      longitude NUMERIC (8, 5)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
      start_time TIMESTAMP PRIMARY KEY,
      hour INT,
      day INT,
      week INT,
      month INT,
      year INT,
      weekday INT
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users ( id, first_name, last_name, gender, level )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
    INSERT INTO songs ( id, title, artist_id, year, duration )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists ( id, name, location, latitude, longitude )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time ( start_time, hour, day, week, month, year, weekday )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT songs.id as songid, artists.id as artistid
    FROM songs JOIN artists ON songs.artist_id = artists.id
    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS


create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
