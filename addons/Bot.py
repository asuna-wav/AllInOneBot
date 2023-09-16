import discord
import os
import asyncio
import ezcord

from discord.commands import ApplicationContext
from discord.errors import DiscordException

from .Log import Logger
from discord.ext import commands, tasks
from dotenv import load_dotenv


class Bot(ezcord.PrefixBot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("-"), intents=discord.Intents.all(), ready_event=None)
        os.system("cls" if os.name == "nt" else "clear")
        self.load_all_cogs()

    def load_cogs(self, directory: str) -> None:
        self.log = Logger().log
        for filename in os.listdir(f"{directory}"):
            if filename.endswith(".py"):
                self.load_extension(f"{directory}.{filename[:-3]}")
                self.log(f"Loaded " + directory + "." + filename[:-3])
                
    def load_subdir(self, root_dir: str) -> None:
        self.log = Logger().log
        for sub in os.scandir(root_dir):
            if sub.is_dir():
                if sub.name == "__pycache__":
                    return
                for item in os.scandir(sub.path):
                    if item.is_file():
                        if item.name == "__init__":
                            return
                        if item.name.endswith('.py'):
                            self.log(f"Loaded {root_dir}.{sub.name}.{item.name[:-3]}")
                        self.load_extension(f"{root_dir}.{sub.name}.{item.name[:-3]}")

    def load_all_cogs(self):
        self.load_cogs("Events")
        self.load_subdir("modules")

    async def on_ready(self):
        self.log = Logger().log
        self.log(f"Logged in as {self.user} ({self.user.id})")
        await self.sync_commands()
        await self.change_presence(
            activity=discord.CustomActivity(name="🌊 :: Loading"), status=discord.Status.idle
        )
        await asyncio.sleep(5)

        await self.change_presence(
            activity=discord.CustomActivity(
                name="⚙️ :: Release soon..."
            )
        )

    async def on_connect(self):
        self._heartbeat.start()

    async def on_disconnect(self):
        self.log = Logger().log
        self.log("Logout detected")

    async def on_application_command_error(self, ctx: ApplicationContext, exception: DiscordException) -> None:
        embed: discord.Embed = discord.Embed(
            title="❌ • Error",
            description=f"### 🚀 :: Important Informations\n\n❌ :: Error: ```py\n{exception}```\n👤 :: Ausführer {ctx.author.mention} | {ctx.author} ({ctx.author.id})\n🌊 :: Command ``/{ctx.command}``",
        )
        await self.get_channel(1152299976362303548).send(embed=embed)
        self.log(exception)

    def run(self):
        load_dotenv()
        if len(os.getenv("TOKEN")):
            super().run(os.getenv("TOKEN"))
        else:
            raise Exception("Invalid Token")
        
    @tasks.loop(minutes=5)
    async def _heartbeat(self):
        if self._heartbeat.current_loop == 0:
            return
        
        self.log = Logger().log
        self.log(f"Heartbeat - {round(self.latency * 1000)}ms")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        await ctx.message.delete()
        reloaded = []
        not_reloaded = []

        for file in os.listdir(f"modules.utils"):
            if file.endswith(".py"):
                try:
                    self.reload_extension(f"modules.utils.{file[:-3]}")
                    reloaded.append(f"✅ :: {file[:-3]}")
                except Exception as e:
                    not_reloaded.append(f"❌ {file[:-3]}: ```py\n{e}```")

        for file in os.listdir(f"Events"):
            if file.endswith(".py"):
                try:
                    self.reload_extension(f"Events.{file[:-3]}")
                    reloaded.append(f"✅ :: {file[:-3]}")
                except Exception as e:
                    not_reloaded.append(f"❌ {file[:-3]}: ```py\n{e}```")

        embed = discord.Embed(
            title="⚙️・COGS GELADEN",
            description="\n".join(reloaded),
            color=discord.Colour.embed_background(),
        )
        if not_reloaded:
            embed.add_field(name="Error beim Reloaden:", value="\n".join(not_reloaded))
        await ctx.send(embed=embed)