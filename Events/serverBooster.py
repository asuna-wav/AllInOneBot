import discord

from addons.Database import DBChannel

from discord.ext import commands
from colorama import Fore

class Booster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBChannel()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.premium_since is None and after.premium_since is not None:
            channel_id = await self.db.get(after.guild.id, "boost")
            booster = after
            nachricht = f"🌊 {booster.mention}, thanks for Boosting our Discord Server!\n★ {after.guild} is now at ``{after.guild.premium_subscription_count}`` Boost/s! 💙"

            channel = after.guild.get_channel(channel_id)

            if channel is not None:
                await channel.send(nachricht)
            else:
                return print(Fore.RED + f'[BOOST]' + Fore.CYAN + '::' + Fore.LIGHTBLUE_EX + 'I failed to send the Boost Message, because the Boost Channel could not be found.')

def setup(bot):
    bot.add_cog(Booster(bot))