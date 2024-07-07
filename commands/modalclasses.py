import discord
from discord.ui.input_text import InputText
from discord.ui.item import Item

class ClaimBBView(discord.ui.Modal):
    def __init__(self, ctx: discord.ApplicationContext, amt, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="CURRENT LOCATION", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="WHERE DO YOU NEED TO GO", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="GENDER NEEDED", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="EXTRA DETAILS", style=discord.InputTextStyle.long))
        self.ctx = ctx
        self.amt = amt
    

    async def callback(self, interaction: discord.Interaction):
        class ClaimBBButton(discord.ui.View):
            def __init__(self, *items: Item, timeout: float | None = 10800, disable_on_timeout: bool = False, ctx = self.ctx, amt: int):
                super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)
                self.ctx = ctx
                self.begin = 0
    
            @discord.ui.button(style=discord.ButtonStyle.green, label="I GOT YOU COVERED BATTLE BUDDY!")
            async def callback(self, button: discord.ui.Button, interaction:discord.Interaction, amt: int = self.amt):
                if self.begin + 1 == amt:
                    button.disabled = True
                    button.label = "ALL SPOTS CLAIMED!"
                    await message.edit_original_response(view=self)
                    await self.ctx.author.send(f"{interaction.user.mention} is on the way")
                    await interaction.respond(f"We have let {self.ctx.author} know that you are on the way!", ephemeral=True)
                else:
                    self.begin += 1
                    await self.ctx.author.send(f"{interaction.user.mention} is on the way")
                    await interaction.respond(f"We have let {self.ctx.author} know that you are on the way!", ephemeral=True)
        
        embed = discord.Embed(title="BATTLE BUDDY REQUESTED")
        embed.set_footer(text=f"Requested by: {self.ctx.author.display_name} | {self.amt} battle buddies requested")
        embed.add_field(name="Current Location: ", value=self.children[0].value, inline=False)
        embed.add_field(name="Destination: ", value=self.children[1].value, inline=False)
        embed.add_field(name="Gender Needed: ", value=self.children[2].value, inline=False)
        embed.add_field(name="Extra Details: ", value=self.children[3].value, inline=False)
        message = await interaction.response.send_message(embeds=[embed], view=ClaimBBButton(amt=self.amt))


class wtsModal(discord.ui.Modal):
    def __init__(self, *children: InputText, title: str, custom_id: str | None = None, timeout: float | None = None) -> None:
        super().__init__(*children, title=title, custom_id=custom_id, timeout=timeout)
        self.add_item(discord.ui.InputText(label="Selling", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Price", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="WTS")
        embed.add_field(name="Selling", value=self.children[0].value, inline=False)
        embed.add_field(name="Price", value="$" + self.children[1].value, inline=False)

        async def callback(self, interaction: discord.Interaction):
        
            class ClaimButton(discord.ui.View):
                def __init__(self, *items: Item, timeout: float | None = 10800, disable_on_timeout: bool = False, ctx = self.ctx, amt: int):
                    super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)
                    self.ctx = ctx
                    self.begin = 0
        
                @discord.ui.button(style=discord.ButtonStyle.green, label="Claim!")
                async def callback(self, button: discord.ui.Button, interaction:discord.Interaction, amt: int = self.amt, item = self.children[0].value):
                    if self.begin + 1 == amt:
                        button.disabled = True
                        button.label = "SOLD OUT"
                        await message.edit_original_response(view=self)
                        await self.ctx.author.send(f"{interaction.user.mention} is on the way for {item}")
                        await interaction.respond(f"We have let {self.ctx.author} know that you are on the way!", ephemeral=True)
                    else:
                        self.begin += 1
                        await self.ctx.author.send(f"{interaction.user.mention} is on the way")
                        await interaction.respond(f"We have let {self.ctx.author} know that you are on the way!", ephemeral=True)
                    message = await interaction.response.send_message(embeds=[embed], view=ClaimButton(amt=self.amt))