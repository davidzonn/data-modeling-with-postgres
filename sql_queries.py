# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS \"user\""
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
      id INT PRIMARY KEY,
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
    CREATE TABLE IF NOT EXISTS \"user\" (
      id INT PRIMARY KEY,
      first_name VARCHAR,
      last_name VARCHAR,
      gender CHAR(1),
      level VARCHAR
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS song (
      id VARCHAR PRIMARY KEY,
      title VARCHAR,
      artist_id VARCHAR,
      year INT,
      duration NUMERIC (20, 5)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist (
      id VARCHAR PRIMARY KEY,
      name VARCHAR,
      location VARCHAR,
      latitude NUMERIC (8, 5),
      longitude NUMERIC (8, 5)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
      start_time timestamp PRIMARY KEY,
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
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]