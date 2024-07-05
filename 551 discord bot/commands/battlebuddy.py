import discord
from commands.modalclasses import ClaimBBView

battlebuddy = discord.SlashCommandGroup("battle-buddy", "commands for requesting battle buddies")

@battlebuddy.command(name="request", description="Request a battle buddy")
async def request(ctx: discord.ApplicationContext):
    await ctx.send_modal(ClaimBBView(ctx, ctx.channel, title="BATTLE BUDDY REQUEST FORM"))