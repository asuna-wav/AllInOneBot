import discord

from discord.ext import commands

from addons.Embed import emb

from discord.commands import SlashCommandGroup

TYPELIST = ["🟢 Online", "🌙 Abwesend", "🔴 DND"]
ACTIVITYLIST = ["⚙️ Custom", "🎮 Gaming", "👀 Watching", "👂 Listening", "🌊 Competing"]


class Admin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    admin_group = SlashCommandGroup(
        name="admin",
        description="🌊 > Admin Commands, from the Aquaecho Bot",
        guild_ids=[1152285260793520228],
    )

    @admin_group.command(name="status", description="🤖 > Change the Bot presence!")
    @discord.default_permissions(administrator=True)
    @discord.option(
        name="type",
        description="⚙️ > What status do u want to change to?",
        choices=TYPELIST,
        required=True,
    )
    @discord.option(
        name="activity",
        description="🎮 > What activity do u want to change to?",
        choices=ACTIVITYLIST,
        required=True,
    )
    @discord.option(
        name="status", description="📝 > What should the text be?", required=True
    )
    async def _status(self, ctx, type: str, status: str, activity: str):
        if type == TYPELIST[0] and activity == ACTIVITYLIST[0]:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.CustomActivity(name=status)
            )
        if type == TYPELIST[1] and activity == ACTIVITYLIST[0]:
            await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.CustomActivity(name=status)
            )
        if type == TYPELIST[2] and activity == ACTIVITYLIST[0]:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.CustomActivity(name=status)
            )
        if type == TYPELIST[0] and activity == ACTIVITYLIST[1]:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.Game(name=status),
            )
        if type == TYPELIST[1] and activity == ACTIVITYLIST[1]:
            await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.Game(name=status),
            )
        if type == TYPELIST[2] and activity == ACTIVITYLIST[1]:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.Game(
                    name=status
                ),
            )
        if type == TYPELIST[0] and activity == ACTIVITYLIST[2]:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.ActivityType.watching(
                    name=status
                ),
            )
        if type == TYPELIST[1] and activity == ACTIVITYLIST[2]:
            await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.ActivityType.watching(
                    name=status
                ),
            )
        if type == TYPELIST[2] and activity == ACTIVITYLIST[2]:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.ActivityType.watching(
                    name=status
                ),
            )
        if type == TYPELIST[0] and activity == ACTIVITYLIST[3]:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.ActivityType.listening(
                    name=status
                ),
            )
        if type == TYPELIST[1] and activity == ACTIVITYLIST[3]:
            await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.ActivityType.listening(
                    name=status
                ),
            )
        if type == TYPELIST[2] and activity == ACTIVITYLIST[3]:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.ActivityType.listening(
                    name=status
                ),
            )
        if type == TYPELIST[0] and activity == ACTIVITYLIST[4]:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.ActivityType.competing(
                    name=status
                ),
            )
        if type == TYPELIST[1] and activity == ACTIVITYLIST[4]:
            await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.ActivityType.competing(
                    name=status
                ),
            )
        if type == TYPELIST[2] and activity == ACTIVITYLIST[4]:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.ActivityType.competing(
                    name=status
                ),
            )
        await emb.info(ctx=ctx, titel=f"🌊 > Status changed", description=f"🌙 STATUS :: {str(type)}\n⚙️ ACTIVITY :: {str(activity)}\n📝 TEXT :: {str(status)}")


def setup(bot):
    bot.add_cog(Admin(bot))
