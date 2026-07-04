CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    signup_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS songs (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    artist TEXT NOT NULL,
    genre TEXT NOT NULL,
    duration_sec INTEGER NOT NULL CHECK (duration_sec > 0),
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS song_plays (
    play_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    song_id INTEGER NOT NULL REFERENCES songs(song_id),
    played_at TIMESTAMP NOT NULL,
    device TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_song_plays_user_id ON song_plays(user_id);
CREATE INDEX IF NOT EXISTS idx_song_plays_song_id ON song_plays(song_id);
CREATE INDEX IF NOT EXISTS idx_song_plays_played_at ON song_plays(played_at);
