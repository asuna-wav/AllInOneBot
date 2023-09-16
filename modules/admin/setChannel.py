import discord

from addons.Database import DBChannel
from addons.Embed import emb

from discord.ext import commands
from discord.commands import SlashCommandGroup


class setChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBChannel()
        self.yes = "<:A_yes:1152285335649255654>"
        self.no = "<:A_no:1152285327986274384>"
        
    set_channel_group = SlashCommandGroup(
        name="setchannel",
        description="💙 Edit the Channel Database with Commands!",
        default_member_permissions=discord.Permissions(administrator=True),
    )

    @set_channel_group.command(
        name="boost",
        description="🚀 > Edit the Boost Log Channel!",
    )
    @discord.option(name="channel", description="📥 > The Channel!", required=True)
    async def _boost_channel_set(self, ctx, channel: discord.TextChannel):
        await self.db.check(guild_id=ctx.guild.id)
        await self.db.set(channel="boost", id=channel.id, guild=ctx.guild.id)

        await emb.info(ctx, f">>> {self.yes} Dein Boost Channel ist nun {channel.mention}!")
        
    @set_channel_group.command(
        name="welcome",
        description="👋 > Edit the Welcome Log Channel!",
    )
    @discord.option(name="channel", description="📥 > The Channel!", required=True)
    async def _boost_channel_set(self, ctx, channel: discord.TextChannel):
        await self.db.check(guild_id=ctx.guild.id)
        await self.db.set(channel="welcome", id=channel.id, guild=ctx.guild.id)

        await emb.info(ctx, f">>> {self.yes} Dein Welcome Channel ist nun {channel.mention}!")
        
    @set_channel_group.command(
        name="log",
        description="⚒️ > Edit the Moderation Log Channel!",
    )
    @discord.option(name="channel", description="📥 > The Channel!", required=True)
    async def _boost_channel_set(self, ctx, channel: discord.TextChannel):
        await self.db.check(guild_id=ctx.guild.id)
        await self.db.set(channel="log", id=channel.id, guild=ctx.guild.id)

        await emb.info(ctx, f">>> {self.yes} Dein Log Channel ist nun {channel.mention}!")
        
    @set_channel_group.command(
        name="error",
        description="❌ > Edit the Error Log Channel!",
    )
    @discord.option(name="channel", description="📥 > The Channel!", required=True)
    async def _boost_channel_set(self, ctx, channel: discord.TextChannel):
        await self.db.check(guild_id=ctx.guild.id)
        await self.db.set(channel="error", id=channel.id, guild=ctx.guild.id)

        await emb.info(ctx, f">>> {self.yes} Dein Error Channel ist nun {channel.mention}!")


def setup(bot):
    bot.add_cog(setChannel(bot))
