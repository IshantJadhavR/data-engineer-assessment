# Schema Documentation

## Tables

### `users`

Stores streaming platform user records.

- `user_id` integer primary key
- `full_name` text
- `email` text
- `country` text
- `signup_date` date

### `songs`

Stores song metadata.

- `song_id` integer primary key
- `song_name` text
- `artist` text
- `genre` text
- `duration_sec` integer
- `release_date` date

### `song_plays`

Stores play events and links each event to one user and one song.

- `play_id` integer primary key
- `user_id` integer foreign key to `users.user_id`
- `song_id` integer foreign key to `songs.song_id`
- `played_at` timestamp
- `device` text
- `city` text

## Relationships

- One user can have many song plays
- One song can appear in many song plays
- `song_plays` is the fact table

## Design choice

This is a classic star-like relational design with two dimension tables (`users`, `songs`) and one event table (`song_plays`). It is intentionally simple so the core SQL patterns are easy to explain during review.
