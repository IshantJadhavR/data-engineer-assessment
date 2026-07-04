-- 1) Join query: users, songs, and song_plays
SELECT
    sp.play_id,
    u.user_id,
    u.full_name,
    s.song_id,
    s.song_name,
    s.artist,
    sp.played_at,
    sp.device,
    sp.city
FROM song_plays sp
JOIN users u
    ON sp.user_id = u.user_id
JOIN songs s
    ON sp.song_id = s.song_id
ORDER BY sp.played_at DESC, sp.play_id DESC;

-- 2) Total plays per song
SELECT
    s.song_id,
    s.song_name,
    s.artist,
    COUNT(*) AS total_plays
FROM song_plays sp
JOIN songs s
    ON sp.song_id = s.song_id
GROUP BY s.song_id, s.song_name, s.artist
ORDER BY total_plays DESC, s.song_name;

-- 3) Total plays per user
SELECT
    u.user_id,
    u.full_name,
    COUNT(*) AS total_plays
FROM song_plays sp
JOIN users u
    ON sp.user_id = u.user_id
GROUP BY u.user_id, u.full_name
ORDER BY total_plays DESC, u.full_name;

-- 4) Top 10 most-played songs
SELECT
    s.song_id,
    s.song_name,
    s.artist,
    COUNT(*) AS total_plays
FROM song_plays sp
JOIN songs s
    ON sp.song_id = s.song_id
GROUP BY s.song_id, s.song_name, s.artist
ORDER BY total_plays DESC, s.song_name
LIMIT 10;

-- 5) Each user's most recently played song
WITH ranked_plays AS (
    SELECT
        u.user_id,
        u.full_name,
        s.song_id,
        s.song_name,
        sp.played_at,
        ROW_NUMBER() OVER (
            PARTITION BY u.user_id
            ORDER BY sp.played_at DESC, sp.play_id DESC
        ) AS rn
    FROM song_plays sp
    JOIN users u
        ON sp.user_id = u.user_id
    JOIN songs s
        ON sp.song_id = s.song_id
)
SELECT
    user_id,
    full_name,
    song_id,
    song_name,
    played_at
FROM ranked_plays
WHERE rn = 1
ORDER BY user_id;

-- 6) Verification counts
SELECT 'users' AS table_name, COUNT(*) AS row_count FROM users
UNION ALL
SELECT 'songs' AS table_name, COUNT(*) AS row_count FROM songs
UNION ALL
SELECT 'song_plays' AS table_name, COUNT(*) AS row_count FROM song_plays;
