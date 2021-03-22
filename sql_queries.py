# DROP TABLES

songplay_table_drop = "DROP TABLE If EXISTS songplays"
user_table_drop = "DROP TABLE If EXISTS users"
song_table_drop = "DROP TABLE If EXISTS songs"
artist_table_drop = "DROP TABLE If EXISTS artists"
time_table_drop = "DROP TABLE If EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id serial PRIMARY KEY, 
                                start_time bigint NOT NULL, 
                                user_id int NOT NULL, 
                                level varchar(255), 
                                song_id varchar(255), 
                                artist_id varchar(255), 
                                session_id int NOT NULL, 
                                location varchar(255), 
                                user_agent varchar(255));
                         """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                            user_id int PRIMARY KEY,
                            first_name varchar(255) NOT NULL,
                            last_name varchar(255) NOT NULL,
                            gender char,
                            level varchar(255));
                    """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                            song_id varchar(255) PRIMARY KEY, 
                            title varchar(255), 
                            artist_id varchar(255), 
                            year int, 
                            duration float);
                      """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                            artist_id varchar(255) PRIMARY KEY, 
                            name varchar(255), 
                            location varchar(255), 
                            latitude float, 
                            longitude float);
                        """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                            start_time timestamp PRIMARY KEY, 
                            hour int NOT NULL, 
                            day int NOT NULL, 
                            week int NOT NULL, 
                            month int NOT NULL, 
                            year int NOT NULL, 
                            weekday varchar NOT NULL);
                        """)


# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
                                start_time, 
                                user_id, 
                                level, 
                                song_id, 
                                artist_id,
                                session_id, 
                                location, 
                                user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                           """)

user_table_insert = ("""INSERT INTO users(
                                user_id, 
                                first_name, 
                                last_name, 
                                gender, 
                                level) VALUES(%s,%s,%s,%s,%s)
                                       ON CONFLICT(user_id) DO UPDATE SET first_name = excluded.first_name,
                                                                          last_name = excluded.last_name,
                                                                          gender = excluded.gender,
                                                                          level = excluded.level;
                      """)

song_table_insert = ("""INSERT INTO songs(
                                song_id, 
                                title, 
                                artist_id, 
                                year, 
                                duration) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING
                     """)

artist_table_insert = ("""INSERT INTO artists(
                                 artist_id, 
                                 name, 
                                 location, 
                                 latitude, 
                                 longitude) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO
                                    UPDATE SET location = excluded.location,
                                               latitude = excluded.latitude,
                                               longitude = excluded.longitude

                        """)


time_table_insert = ("""INSERT INTO time(
                               start_time, 
                               hour, 
                               day, 
                               week, 
                               month, 
                               year, 
                               weekday) VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING;
                     """)

# FIND SONGS

song_select = (""" SELECT s.song_id, a.artist_id FROM songs AS s
                        LEFT OUTER JOIN artists AS a 
                        ON s.artist_id = a.artist_id
                        WHERE s.title = %s AND a.name = %s AND s.duration = %s;
                """)



# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

