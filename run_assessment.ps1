$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "Starting PostgreSQL container..." -ForegroundColor Cyan
docker compose up -d

Write-Host "Cleaning raw CSV..." -ForegroundColor Cyan
python 05_Source_Code/python/clean_song_plays.py `
  --input 05_Source_Code/data/raw/song_plays_raw.csv `
  --output 05_Source_Code/data/cleaned/song_plays_clean.csv

Write-Host "Creating database..." -ForegroundColor Cyan
docker compose exec -T postgres psql -U postgres -f /workspace/05_Source_Code/sql/00_create_database.sql

Write-Host "Creating tables..." -ForegroundColor Cyan
docker compose exec -T postgres psql -U postgres -d music_streaming_db -f /workspace/05_Source_Code/sql/01_create_tables.sql

Write-Host "Loading data..." -ForegroundColor Cyan
docker compose exec -T postgres psql -U postgres -d music_streaming_db -f /workspace/05_Source_Code/sql/02_load_data.sql

Write-Host "Running queries..." -ForegroundColor Cyan
docker compose exec -T postgres psql -U postgres -d music_streaming_db -f /workspace/05_Source_Code/sql/03_queries.sql

Write-Host "Done. Take screenshots of the query output and add your GitHub link in 01_GitHub_Links.txt." -ForegroundColor Green
