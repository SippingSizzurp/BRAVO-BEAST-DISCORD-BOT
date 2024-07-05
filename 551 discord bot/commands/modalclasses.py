import discord
from discord.ui.item import Item

class ClaimBBView(discord.ui.Modal):
    def __init__(self, ctx: discord.ApplicationContext, ch, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="CURRENT LOCATION", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="WHERE DO YOU NEED TO GO", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="EXTRA DETAILS", style=discord.InputTextStyle.long))
        self.ctx = ctx
        self.ch = ch
    

    async def callback(self, interaction: discord.Interaction):
        class ClaimBBButton(discord.ui.View):
            def __init__(self, *items: Item, timeout: float | None = 10800, disable_on_timeout: bool = False, ctx = self.ctx):
                super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)
                self.ctx = ctx
    
            @discord.ui.button(style=discord.ButtonStyle.green, label="I'M COMING BATTLE BUDDY!")
            async def callback(self, button: discord.ui.Button, interaction:discord.Interaction):
                button.disabled = True
                await message.edit_original_response(view=self)
                await self.ctx.author.send(f"{interaction.user.mention} is on the way")
                await interaction.respond(f"We have let {self.ctx.author} know that you are on the way!", ephemeral=True)
        
        embed = discord.Embed(title="BATTLE BUDDY REQUESTED")
        embed.set_footer(text=f"Requested by: {self.ctx.author.display_name}")
        embed.add_field(name="Current Location: ", value=self.children[0].value, inline=False)
        embed.add_field(name="Destination: ", value=self.children[1].value, inline=False)
        embed.add_field(name="Extra Details: ", value=self.children[2].value, inline=False)
        message = await interaction.response.send_message(embeds=[embed], view=ClaimBBButton())
        