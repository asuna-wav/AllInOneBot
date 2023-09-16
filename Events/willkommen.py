import discord

from addons.Database import DBChannel


from discord.ext import commands


class WelcomeCard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBChannel()

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = await self.db.get(member.guild.id, "welcome")

        try:
            channel = discord.utils.get(member.guild.channels, id=channel_id)
        except:
            return

        await channel.send(
            f"🌊 Welcome {member.mention}!\n★ Du bist das {member.guild.member_count} Mitglied auf diesem Server!"
        )


def setup(bot):
    bot.add_cog(WelcomeCard(bot))
