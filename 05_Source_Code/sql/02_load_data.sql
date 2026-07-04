COPY users(user_id, full_name, email, country, signup_date)
FROM '/workspace/05_Source_Code/data/raw/users.csv'
WITH (FORMAT csv, HEADER true);

COPY songs(song_id, song_name, artist, genre, duration_sec, release_date)
FROM '/workspace/05_Source_Code/data/raw/songs.csv'
WITH (FORMAT csv, HEADER true);

COPY song_plays(play_id, user_id, song_id, played_at, device, city)
FROM '/workspace/05_Source_Code/data/cleaned/song_plays_clean.csv'
WITH (FORMAT csv, HEADER true);
