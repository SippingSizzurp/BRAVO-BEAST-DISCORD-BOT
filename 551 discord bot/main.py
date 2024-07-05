import discord
import asyncio

from commands.utility import utility
from commands.market import market
from commands.battlebuddy import battlebuddy

bot = discord.Bot(intents=discord.Intents.all(), help_command=None)

async def change_status():
    activities = [
        discord.Activity(type=discord.ActivityType.watching, name="BETA TESTING"),
        discord.Activity(type=discord.ActivityType.listening, name="/HELP"),
        discord.Activity(type=discord.ActivityType.playing, name="Made by @sippingsizzurp")
    ]

    while True:
        for activity in activities:
            await bot.change_presence(activity=activity)
            await asyncio.sleep(10)

@bot.event
async def on_ready():
    print(f"LOGGED IN AS {bot.user.name}")

bot.add_application_command(utility)
bot.add_application_command(market)
bot.add_application_command(battlebuddy)
bot.run("")