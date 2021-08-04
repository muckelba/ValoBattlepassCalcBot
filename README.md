# Valorant Battlepass Calculator Discord Bot

Simple python discord bot to calculate your battlepass progress.

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

![image](https://user-images.githubusercontent.com/34460584/128231983-ab3dd4ea-dd2c-4e92-8c0c-dfc1b5fb737a.png)

The first argument is your current level, the second one is your current XP within that level, the third argument is your level goal (ususally thats 50 or 55), the fourth one is optional and calculates without the weekly XP. Just write any character, it just have to be there.

## Data

Battlepass XP values are taken from [this tweet](https://twitter.com/Shiick/status/1408007768699768839) and might need to adjusted each season. If i dont do it, just update the `data.json` file.


## Credit

Some calculations are taken from this [GitHub project](https://github.com/SamueldaCostaAraujoNunes/BattlePass-Calculator-for-VALORANT/).


## Disclaimer

This is a fanmade tool, i am not affiliated with VALORANT or RIOT GAMES in anyway, any (copy)right belongs to them.