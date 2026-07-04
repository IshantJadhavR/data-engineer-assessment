from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

users = [
    (1, "Alice Johnson", "alice@example.com", "US", "2025-05-01"),
    (2, "Brian Patel", "brian@example.com", "IN", "2025-05-03"),
    (3, "Chen Li", "chen@example.com", "SG", "2025-05-05"),
    (4, "Diana Khan", "diana@example.com", "UK", "2025-05-06"),
    (5, "Ethan Gomez", "ethan@example.com", "US", "2025-05-07"),
]

songs = [
    (1, "Sunrise Echo", "The North", "Ambient", 210, "2024-11-15"),
    (2, "Night Drive", "Neon Lane", "Synthwave", 195, "2024-09-08"),
    (3, "River Flow", "Mina Hart", "Lo-Fi", 180, "2024-12-22"),
    (4, "City Lights", "Orbit Nine", "Pop", 224, "2025-01-10"),
    (5, "Paper Planes", "Indie Atlas", "Indie", 201, "2024-08-19"),
    (6, "Golden Hour", "Ari Vale", "Pop", 232, "2025-02-14"),
    (7, "Static Dreams", "Pixel Soul", "Electro", 188, "2024-10-05"),
    (8, "Blue Horizon", "Luna Reed", "Chill", 244, "2024-12-01"),
    (9, "Ember Trail", "Wild North", "Folk", 207, "2025-03-11"),
    (10, "Quiet Storm", "Harbor Note", "Instrumental", 260, "2024-07-30"),
]

song_plays = [
    (1, 1, 1, "2025-07-01 08:30:00", "mobile", "delhi"),
    (2, 1, 4, "2025-07-01 09:05:00", "Web", "Delhi"),
    (3, 2, 2, "2025/07/01 10:15", "mobile", "mumbai"),
    (4, 2, 3, "2025-07-01 10:45:00", "tablet", "mumbai"),
    (5, 3, 6, "2025-07-01 11:20:00", "MOBILE", "singapore"),
    (6, 4, 2, "2025-07-01 12:00:00", "web", "London"),
    (7, 5, 10, "2025-07-01 12:45:00", "Mobile", "new york"),
    (8, 1, 2, "2025-07-02 08:10:00", "web", "Delhi"),
    (9, 3, 1, "2025-07-02 08:55:00", "mobile", "singapore"),
    (10, 4, 7, "2025-07-02 09:25:00", "WEB", "London"),
    (11, 2, 6, "2025-07-02 09:40:00", "tablet", "Mumbai"),
    (12, 5, 4, "2025-07-02 10:30:00", "mobile", "New York"),
    (2, 1, 4, "2025-07-01 09:05:00", "Web", "Delhi"),  # duplicate
    (13, 3, 5, "2025-07-02 11:05:00", "web", "Delhi"),
    (14, 2, "", "2025-07-02 11:40:00", "mobile", "Delhi"),  # missing song_id
    (15, 2, 5, "", "mobile", "Delhi"),  # missing timestamp
    (16, 4, 8, "2025-07-02 12:15:00", "Mobile", "London"),
    (4, 2, 3, "2025-07-01 10:45:00", "tablet", "mumbai"),  # duplicate
    (19, 3, 9, "2025-07-03 08:20:00", "mobile", "Singapore"),
    (20, 1, 6, "2025-07-03 08:50:00", "WEB", "Delhi"),
    (21, 5, 1, "2025-07-03 09:10:00", "Mobile", "New York"),
    (22, 2, 10, "2025-07-03 09:35:00", "web", "Mumbai"),
    (23, 4, 4, "2025-07-03 10:00:00", "tablet", "London"),
    (24, 1, 2, "2025-07-03 10:25:00", "mobile", "delhi"),
    (25, 3, 6, "2025-07-03 10:55:00", "MOBILE", "Singapore"),
]


def write_csv(path: Path, header: list[str], rows: list[tuple]) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


write_csv(RAW_DIR / "users.csv", ["user_id", "full_name", "email", "country", "signup_date"], users)
write_csv(RAW_DIR / "songs.csv", ["song_id", "song_name", "artist", "genre", "duration_sec", "release_date"], songs)
write_csv(
    RAW_DIR / "song_plays_raw.csv",
    ["play_id", "user_id", "song_id", "played_at", "device", "city"],
    song_plays,
)

print(f"Sample CSV files written to {RAW_DIR}")
