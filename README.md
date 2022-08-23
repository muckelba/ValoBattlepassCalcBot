# Valorant Battlepass Calculator Discord Bot

Simple python discord bot to calculate your battlepass progress.

## Public Bot

There's now a public bot hosted by me. Invite it to your server whith [this link](https://discord.com/oauth2/authorize?client_id=874989994232651856&&scope=bot). Join [this Discord](https://discord.gg/SUmGjUG7Mb) for help and updates.


## Installation

Python 3.6+ required, only tested 3.8!

Install the requirements:
```bash
pip install -r requirements.txt
```

Copy and rename `config.ini.example` to `config.ini` and paste the discord bottoken. 

Set your language, currently available languages are only `en` and `de`, PRs with more languages are welcome!

Run the bot:
```bash
python bot.py
```

## Usage

The usage is pretty straight forward: 

![image](https://user-images.githubusercontent.com/34460584/129038598-2e55b7b0-7f44-49e6-b195-6db56354df8b.png)

The first argument is your current level, the second one is your current XP within that level, the third argument is your level goal (ususally thats 50 or 55), the fourth one is optional and calculates without the future weekly XP. Just write any character, it just has to be there.

## Data

Battlepass XP values are taken from [this tweet](https://twitter.com/shiick/status/1562095421031432192) and might need to adjusted each season. If i dont do it, just update the `data.json` file.


## Credit

Some calculations are taken from this [GitHub project](https://github.com/SamueldaCostaAraujoNunes/BattlePass-Calculator-for-VALORANT/).


## Disclaimer

This is a fanmade tool, i am not affiliated with VALORANT or RIOT GAMES in any way, every (copy)right belongs to them.