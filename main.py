import discord
import asyncio

from commands.utility import utility
from commands.market import market
from commands.battlebuddy import battlebuddy

bot = discord.Bot(intents=discord.Intents.all(), help_command=None)

async def change_status():
    activities = [
        discord.Activity(type=discord.ActivityType.watching, name="BETA TESTING"),
        discord.Activity(type=discord.ActivityType.playing, name="Made by @sippingsizzurp (PV2 Procopio)")
    ]

    while True:
        for activity in activities:
            await bot.change_presence(activity=activity)
            await asyncio.sleep(10)

@bot.event
async def on_ready():
    asyncio.create_task(change_status())
    print(f"LOGGED IN AS {bot.user.name}")

support = discord.SlashCommandGroup("support")

@support.command(name="open-ticket", description="Opens a support ticket")
async def supportt(ctx):

    category = discord.utils.get(ctx.guild.categories, name='Tickets')
    if not category:
        category = await ctx.guild.create_category('Tickets')

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    ticket = await ctx.guild.create_text_channel(name=f"ticket-{ctx.author.name}", category=category)

    embed = discord.Embed(title="New Ticket",
                          description=f"Hi {ctx.author.mention}, Please provide a brief description of your needs.",
                          color=0x00ff00)
    embed.add_field(name="Close Ticket", value="Click the ✖️ reaction to close this ticket.", inline=False)
    embed.add_field(name="Mark as Solved", value="Click the ✅ reaction to mark this ticket as solved.", inline=False)
    message = await ticket.send(embed=embed)

    await message.add_reaction('✖')
    await message.add_reaction('✅')

    await ctx.respond(f"{ticket.mention} has been created", ephemeral=True)


    @bot.event
    async def on_raw_reaction_add(payload):
        if payload.message_id == message.id:
            if str(payload.emoji) == '✖':
                await ticket.delete()
            elif str(payload.emoji) == '✅':
                await ticket.edit(name=f"solved-{ctx.author.name}", category=discord.utils.get(ctx.guild.categories, name='Archived Tickets'))

# bot.add_application_command(utility)
# bot.add_application_command(market)
bot.add_application_command(battlebuddy)
bot.add_application_command(support)
bot.run("")