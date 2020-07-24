# Data Modeling with Postgres

The goal of this project is to create an ETL pipeline in postgres for a music streaming app. It includes the definition and population of fact and dimension tables.

Sparkify is a music streaming startup. This project implements an analytical framework to allow Sparkify to quickly and easily analyse user behaviours from their log data.

In order to provide simplicity, ease of aggregation, and quick results, a *star schema* was implemented.

Songplays is the fact table. It contains the songs played by the user. It contains a reference to the following dimensions which further describe these events:

- **User dimension**, represented by the users table, provides detailed description of the users.
- **Song dimension**, represented by the songs table, provides further information on the songs.
- **Artist dimension**, represented by the artists table, gives information about the artists of the songs.
- **Time dimension**, represented by the time table, provides easy and intuitive access to time and date in different formats.

An ETL process was provided to populate the databases from the logs. This is provided in the etl script which, at the current state, would need to be periodically run (say, from a daemon) to synchronize new logs. The ETL process consists of:

1. processing the song data files:
    The song files, containing information of the songs, is processed and stored in the song and artists tables.
     
2. Aggregating and processing the log data files:
    For the log items, it is filtered by the events of interest (songplays), a lookup is made for each log event for the corresponding songs and artists, users are stored in a unique way, and the events are stored together with the corresponding references in the songplays table.   

Some advantages of this design are: 
- **Simplicity.** The design is very easy to understand by an analytical team.
- **Ease of aggregation.** It is easy to obtain aggregated results and detailed information in the dimension required, without the need of complex chained joins.
- **Quick results.** Simple joins ensure quick reads and aggregations for diverse queries.