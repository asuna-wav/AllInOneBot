import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, option

from data.jaildb import JailDatabase

class Jail(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.db = JailDatabase()
        
    jail_group = SlashCommandGroup(
        name="jail",
        description="🔒 | Jail Commands, from the AquaEcho Bot",
        default_member_permissions=discord.Permissions(administrator=True)
    )
    
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await JailDatabase().setup()
        
    @jail_group.command(
        name="add",
        description="🔒 > Add a user to the Jail!"
    )
    async def _jail_add(self, ctx: discord.ApplicationContext, user: discord.User, time: int, reason: str):
        await ctx.respond('🔒 | Under *Development*!', ephemeral=True)
def setup(bot: discord.Bot) -> None:
    bot.add_cog(Jail(bot))