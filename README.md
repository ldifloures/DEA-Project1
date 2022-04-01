# Data Modeling with Postgres

## Overview
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, I created a star schema data model using Postgres and built an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Files included
sql_queries.py - This contains the sql scripts that are used to DROP, CREATE, UPDATE tables that is used in the create_tables.py script.  It also contains the song_select script that is used in the etl.py script.
create_queries.py - This script creates the sparkifydb database that will be used to store the song, artist, user, time and songplay data.
etl.py - This script reads the song and log files in to respective fact and dimension tables.

## Load data
step 1 - Open terminal
step 2 - type python create_queries.py and hit enter
step 3 - type python etl.py and hit enter
