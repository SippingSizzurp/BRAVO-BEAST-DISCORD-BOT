import discord
from main import bot

support = discord.SlashCommandGroup("support")

@support.command(name="support", description="Opens a support ticket")
async def supportt(ctx):

    category = discord.utils.get(ctx.guild.categories, name='Tickets')
    if not category:
        category = await ctx.guild.create_category('Tickets')

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    ticket = await ctx.guild.create_text_channel(name=f"ticket-{ctx.author.name}", category=category,
                                                 overwrites=overwrites)

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