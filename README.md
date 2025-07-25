# Telegram-to-Discord

A Python application to forward messages from a Telegram channel to a Discord channel using webhooks.

## Features
- Reads messages from a specified Telegram channel
- Sends messages to a Discord channel via webhook
- Configurable via `config.json`

## Requirements
- Python 3.12+
- Telegram API credentials: https://my.telegram.org/
- Discord webhook URL

## Setup
1. Clone the repository.
2. Copy `config.example.json` to `config.json` and fill in your credentials:
   - Telegram `api_id`, `api_hash`, and `channel_name`
   - Discord webhook `url`
3. (Optional) Use Docker for deployment:
   - Run the script once and login into Telegram to generate the session
   - Build: `docker compose build`
   - Run: `docker compose up`

## Usage
Run the main application:
```bash
pip install telethon requests
cd app
python3 main.py
```

## Configuration
Edit `config.json` with your Telegram and Discord details. See `config.example.json` for format.

## Logging
Logs are written to `app/telegramm_to_discord.log`.

