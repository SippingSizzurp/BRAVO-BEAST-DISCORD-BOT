import discord
from database import Database

market = discord.SlashCommandGroup("market", "market commands")

@market.command(name="set_channel", description="Sets the servers market channel")
async def set_channel(ctx: discord.ApplicationContext, channel: discord.TextChannel):
    Database.update_market_channel("market", channel.id, ctx.guild.id)
    embed = discord.Embed(title="MARKET CHANNEL UPDATED", 
                          description=f"{channel.mention} has been set as the market")
    await ctx.respond(embed=embed)

