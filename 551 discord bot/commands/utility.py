import discord
import sqlite3
from discord.ext import commands
from random import choice
from string import ascii_letters
from database import Database

utility = discord.SlashCommandGroup("utility", "commands that are used for utilities")

@utility.command(name="ping", description="Ping the bot to make sure it is up")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("pong")

@utility.command(name="verify", description="verify to get into the server")
async def verify(ctx: discord.ApplicationContext):
    password = ""

    for i in range(8):
        password += choice(ascii_letters)
    
    Database.add_captcha(password)

    embed1 = discord.Embed(title="CAPTCHA", description=password)
    embed2 = discord.Embed(title="CAPTCHA SENT")

    await ctx.author.send(embed=embed1)
    await ctx.respond(embed=embed2, ephemeral=True)
    role = discord.Guild.get_role(ctx.guild, 1258175200160383037)
    