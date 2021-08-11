import discord
from discord.ext import commands
from datetime import datetime, date
import configparser
import logging
import json
import math
import gettext

logging.basicConfig(
    format='[%(asctime)s] %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

config = configparser.ConfigParser()
config.read('config.ini')

token = config['bot']['token']
language = config['bot']['language']

with open('data.json') as json_file:
    data = json.load(json_file)

translation = gettext.translation('base', './locale', fallback=True, languages=[language])
translation.install()
_ = translation.gettext

client = commands.Bot(command_prefix = "!")


def calculate_level_xp(level):
    if 2 <= level <= 50:
        return 2000 + (level - 2) * 750
    elif 51 <= level <= 55:
        return 36500
    else:
        return 0

def calculate_total_xp(current_level, current_xp):
    result = current_xp

    for i in range(1, current_level):
        result += calculate_level_xp(i)
    return result

async def calc_battlepass(currentlevel, currentxp, maxlevel, withoutweeklies):
    average_unrated_xp = 4200
    spike_rush_xp = 1000
    total_weeks = int(max(data['weeklies']))
    season_end = datetime.strptime(data['season_end'], '%d.%m.%Y').date()
    season_now = datetime.now().date()
    season_left = season_end - season_now
    season_weeks_left = season_left.days / 7

    totalxp = calculate_total_xp(int(currentlevel), int(currentxp))
    xpneeded = calculate_total_xp(int(currentlevel)+1, 0) - totalxp
    totalxpneeded = 0
    for i in range(1, int(maxlevel)+1):
        totalxpneeded += calculate_level_xp(i)

    weeklyxp = 0
    if not withoutweeklies:
        for i in range((total_weeks - math.floor(season_weeks_left)), total_weeks + 1):
            weeklyxp += data['weeklies'][str(i)]

    totalxpneeded = totalxpneeded - (totalxp + weeklyxp)
    spikerushneeded = totalxpneeded / spike_rush_xp
    normalneeded = totalxpneeded / average_unrated_xp
    dailyxpneeded = totalxpneeded / season_left.days
    weeklyxpneeded = totalxpneeded / season_weeks_left
    return totalxp, xpneeded, max(0, totalxpneeded), max(0, math.ceil(spikerushneeded)), max(0, math.ceil(normalneeded)), max( 0, math.ceil(dailyxpneeded)), max(0, math.ceil(weeklyxpneeded))

@client.command()
async def battlepass(ctx, currentlevel=None, currentxp=None, maxlevel=None, withoutweeklies=None):
    usage = _("Usage: `!battlepass [Current level] [Current XP] [Wanted level] [Without weeklies]`")
    try: 
        isinrange = 1 <= int(currentlevel) <= 55
    except:
        await ctx.send(_(":x: Please enter your current level correctly"))
        await ctx.send(usage)
        return

    if not currentlevel or not isinrange:
        await ctx.send_(_(":x: Your entered level is not between 1 and 55"))
        await ctx.send(usage)
        return

    try: 
        isinrange = 0 <= int(currentxp) <= 38000
    except:
        await ctx.send_(_(":x: Please enter your current XP correctly"))
        await ctx.send(usage)
        return

    if not currentxp or not isinrange:
        await ctx.send_(_(":x: Your entered XP is not between 0 and 38,000"))
        await ctx.send(usage)
        return

    try: 
        isinrange = 1 <= int(maxlevel) <= 55
    except:
        await ctx.send_(_(":x: Please enter your wanted level correctly"))
        await ctx.send(usage)
        return

    if not maxlevel or not isinrange:
        await ctx.send_(_(":x: Your entered wanted level is not between 1 and 55"))
        await ctx.send(usage)
        return

    result = await calc_battlepass(currentlevel, currentxp, maxlevel, withoutweeklies)
    if not withoutweeklies:
        note = _(" + Weekly XP")
    else:
        note = ""
    text = f"""
    {_("Total XP")}: `{'{:,}'.format(result[0])}`
    {_("Needed XP for level up")}: `{'{:,}'.format(result[1])}`
    {_("Needed XP for level")} {maxlevel}: `{'{:,}'.format(result[2])}` {note}
    {_("Needed Spikerushes")}: `{result[3]}`
    {_("Needed Normal/Ranked Games")}: `{result[4]}`
    {_("Average daily XP needed")}: `{'{:,}'.format(result[5])}`
    {_("Average weekly XP needed")}: `{'{:,}'.format(result[6])}`
    """
    embed = discord.Embed(title=_("Battlepass Calculator"), description=text, color=16401492)
    embed.set_thumbnail(url="https://esport.uni-bayreuth.de/wp-content/uploads/2020/11/logo_valorant-150x150.png")
    if not withoutweeklies:
        embed.set_footer(icon_url="https://i.imgur.com/wbghHOx.png", text=_("With future completed weeklies"))
    await ctx.send(embed=embed)

# Boot confirmation
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='VALORANT'))
    logging.info(_("Bot is ready"))

client.run(token)