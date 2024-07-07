import discord
from database import Database

market = discord.SlashCommandGroup("market", "market commands")

@market.command(name="wts", description="Make a WTS post")
async def wts(ctx: discord.ApplicationContext, amount: int):
    return

