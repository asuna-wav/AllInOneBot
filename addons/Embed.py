import discord


class emb:
    async def info(
        ctx: discord.ApplicationContext,
        description: str,
        titel: str | None = None,
        color: int | None = 0x697EB7
    ):
        await ctx.channel.send(
            embed=discord.Embed(title=titel, description=description, color=color)
        )
        await ctx.response.send_message(
            embed=discord.Embed(title=titel, description=description, color=color),
            ephemeral=True
        )
    async def info(
        ctx: discord.ApplicationContext,
        description: str,
        titel: str | None = None,
        color: int | None = 0x697EB7,
        eph: bool | None = True,
    ):
        await ctx.response.send_message(
            embed=discord.Embed(title=titel, description=description, color=color),
            ephemeral=eph,
        )

    async def error(
        ctx: discord.ApplicationContext,
        description: str,
        color: int | None = 0xB76969,
        eph: bool | None = True,
    ):
        await ctx.response.send_message(
            embed=discord.Embed(description=description, color=color), ephemeral=eph
        )

    async def custom(ctx: discord.ApplicationContext, title, description, color, eph):
        await ctx.response.send_message(
            embed=discord.Embed(title=title, description=description, color=color),
            ephemeral=eph,
        )
