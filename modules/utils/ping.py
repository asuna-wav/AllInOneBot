import discord

import aiosqlite

import time

from discord.ext import (
    commands
)

from discord.commands import (
    SlashCommandGroup,
    option
)

from addons.Embed import emb

PINGLIST = ["🔒 > Database", "🤖 > Bot"]

class Ping(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        
    help_group = SlashCommandGroup(
        name="help",
        description="⚒️ | Help Commands, from the AquaEcho Bot"
    )
    
    @help_group.command(
        name="ping",
        description="🌊 > Shows the Ping of the Bot"
    )
    @option(name="type", description="⚙️ > What Ping do u want to get", choices=PINGLIST, required=False)
    async def _ping(self, ctx, type: str):
        async with aiosqlite.connect("main.db") as db:
            start_time = time.time()
            
            await db.execute(
                """
                SELECT 1
                """
            )
            
            end_time = time.time()
            
        BOT_PING = round(self.bot.latency * 1000)
        DATABASE_PING = round((end_time - start_time) * 1000)
        
        if type is None:
            return await emb.info(ctx=ctx, description=f"⚙️ • Database :: **{DATABASE_PING}ms**\n🤖 • Bot :: **{BOT_PING}ms**")
        if type == PINGLIST[0]:
            return await emb.info(ctx=ctx, description=f"⚙️ • Database :: **{DATABASE_PING}ms**")
        if type == PINGLIST[1]:
            return await emb.info(ctx=ctx, description=f"🤖 • Bot :: **{BOT_PING}ms**")
        else:
            return await emb.error(ctx=ctx, description=">>> ❌ Invalid Ping Type")
    
        
def setup(bot: discord.Bot) -> None:
    bot.add_cog(Ping(bot))