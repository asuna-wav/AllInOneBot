import discord
from discord.ext import commands
from addons.Database import DBChannel

async def return_channel(self, guild_id: int):
    channel_id = await DBChannel().get(guild_id=guild_id, channel="log")
    if channel_id is not None:
        return self.bot.get_channel(channel_id)
    else:
        return print('Channel could not be found.')

class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        em = discord.Embed(
            title='💬 MESSAGE Deleted',
            description=f'**Deletede MESSAGE from**: {message.author}'
                        f'\r\n**Inhalt der MESSAGE**: {message.content}'
                        f'\r\n**Im Channel**: {message.channel.mention}',
            color=discord.Colour.embed_background()
        )
        channel = await return_channel(self, message.guild.id)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        alist = []
        for m in messages:
            if not str(m.author.mention) in alist:
                alist.append(str(m.author.mention)) 
        async for entry in messages[0].guild.audit_logs(action=discord.AuditLogAction.message_bulk_delete, limit=1):
            embed = discord.Embed(title="💬 Message Deleted", description=f"**Author:** {', '.join(alist)}\n**Channel:** {messages[0].channel.mention} | `{messages[0].channel.id}`\n**Amount:** {len(messages)}\n**Deleted from:** {entry.user.mention}", color=discord.Colour.embed_background())
            channel = await return_channel(self, messages.guild.id)
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        em = discord.Embed(
            title='💬 MESSAGE BEARBEITET',
            description=f'**Bearbeitete MESSAGE from**: {before.author}'
                    f'\r\n**Alte MESSAGE**: {before.content}'
                    f'\r\n**New MESSAGE**: {after.content}',
        			color=discord.Colour.embed_background()
           )
        channel = await return_channel(self, after.guild.id)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if len(before.roles) > len(after.roles):
            role = next(role for role in before.roles if role not in after.roles)
            em = discord.Embed(
                title='👥 ROLE ENTFERNT',
                description=f'**Name**: {before}\r\n**Entfernte ROLE:**: {role.name}',
                color=discord.Colour.embed_background(),
            )

        elif len(after.roles) > len(before.roles):
            role = next(role for role in after.roles if role not in before.roles)
            em = discord.Embed(
                title='👥 ROLE Added',
                description=f'**Name**: {before}\r\n**New ROLE:**: {role.name}',
                color=discord.Colour.embed_background(),
            )

        elif before.nick != after.nick:
            em = discord.Embed(
                title='👥 NICKNAME Changed',
                description=f'**Name**: {before}\r\n**Alter NickName**: {before.nick}\r\n**Newr NickName**: {after.nick}',
                color=discord.Colour.embed_background(),
            )

        else:
            return
        channel = await return_channel(self, after.guild.id)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        em = discord.Embed(
            title='📝 Channel Created',
            description=f'**New Channel**: {channel.mention}\n**Categorey:** {channel.category}',
            color=discord.Colour.embed_background(),
        )
        channel = await return_channel(self, channel.guild.id)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        channel = await return_channel(self, after.guild.id)
        if not before.name == after.name:
            embed = discord.Embed(title="🔎 Changed a Channel Name!", description=f"**Name:** {before.mention} | `{after}`\n**ID:** `{before.id}`\n**Categorie:** {before.category}", color=discord.Colour.embed_background())
            embed.add_field(name="Before:", value=before.name, inline=False)
            embed.add_field(name="After:", value=after.name, inline=False)
            await channel.send(embed=embed)
        if not before.slowmode_delay == after.slowmode_delay:
            embed = discord.Embed(title="🔎 Changed a Channel Name!", description=f"**Name:** {before.mention} | `{after}`\n**ID:** `{before.id}`\n**Categorie:** {before.category}", color=discord.Colour.embed_background())
            embed.add_field(name="Before:", value=before.slowmode_delay, inline=False)
            embed.add_field(name="After:", value=after.slowmode_delay, inline=False)
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        em = discord.Embed(
            title='🔎 CHANNEL Deleted',
            description=f'**Channel got Deleted**: {channel.mention}\n**Categorie:** {channel.category}',
            color=discord.Colour.embed_background()
        )
        channel = await return_channel(self, channel.guild.id)
        await channel.send(embed=em)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        em = discord.Embed(
            title='👥 USER Joined',
            description=f'**User**: {member.name}',
            color=discord.Colour.embed_background()
        )
        channel = await return_channel(self, member.guild.id)
        await channel.send(embed=em)

        ### OPTIONAL THINGS !!
        # role = discord.utils.get(member.guild.roles, id=1152353653861122159)
        # await member.add_roles(role)
        ### ONE MORE FOR A LIST OF ROLES
        # rolelist = [123, 123]
        # for role_id in rolelist:
        #     role = discord.utils.get(member.guild.roles, id=role_id)
        #     await member.add_roles(role)
            
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        em = discord.Embed(
            title='👥 USER Leaved',
            description=f'**User**: {member.name}',
            color=discord.Colour.embed_background()
        )
        channel = await return_channel(self, member.guild.id)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        embed = discord.Embed(title="🔎 ROLE Created", description=f"**Name:** {role.mention} | `{role}`\n**ID:** `{role.id}`", color=role.color)
        channel = await return_channel(self, role.guild.id)
        await channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        embed = discord.Embed(title="🔎 ROLE Deleted", description=f"**Name:** {role.mention} | `{role}`\n**ID:** `{role.id}`", color=role.color)
        channel = await return_channel(self, role.guild.id)
        await channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        channel = await return_channel(self, after.guild.id)
        if not before.name == after.name:
            embed = discord.Embed(title="🔎 ROLENAME Changed", description=f"**Name:** {before.mention} | `{after}`\n**ID:** `{before.id}`", color=after.color)
            embed.add_field(name="Before:", value=before.name, inline=False)
            embed.add_field(name="After:", value=after.name, inline=False)
            await channel.send(embed=embed)
        if not before.color == after.color:
            embed = discord.Embed(title="🔎 ROLECOLOR Changed", description=f"**Name:** {before.mention} | `{after}`\n**ID:** `{before.id}`", color=after.color)
            embed.add_field(name="Before:", value=before.color, inline=False)
            embed.add_field(name="After:", value=after.color, inline=False)
            await channel.send(embed=embed)
        if before.icon is not None and after.icon is not None and before.icon.url != after.icon.url:
            embed = discord.Embed(title="🔎 ROLEICON Changed", color=discord.Color.blue())
            embed.set_thumbnail(url=after.icon.url)
            embed.add_field(name="ROLE", value=after.mention, inline=False)
            embed.add_field(name="ROLEn-ID", value=after.id)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        if not before.name == after.name:
            embed = discord.Embed(title="🔎 SERVER NAME Changed", description=f"**Name:** {after.name}`\n**ID:** `{before.id}`", color=discord.Colour.embed_background())
            embed.add_field(name="Before:", value=before.name, inline=False)
            embed.add_field(name="After:", value=after.name, inline=False)
            channel = await return_channel(self, guild_id=after.guild.id)
            await channel.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        channel = await return_channel(self, after.guild.id)
        for emoji in after:
            if not emoji in before:
                embed = discord.Embed(title="🔎 ROLE Added", description=f"**Name:** {emoji.name} | {emoji}\n**ID:** `{emoji.id}`", color=discord.Colour.embed_background())
                await channel.send(embed=embed)
        for emoji in before:
            if not emoji in after:
                embed = discord.Embed(title="🔎 EMOJI Deleted", description=f"**Name:** {emoji.name} | {emoji}\n**ID:** `{emoji.id}`", color=discord.Colour.embed_background())
                await channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        channel = await return_channel(self, guild_id=guild.id)
        async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1):
            embed = discord.Embed(
                title="👥 USER Banned",
                description=f"**Name:** {user.mention} | `{user}`\n**ID:** `{user.id}`\n**Banned from:** {entry.user.mention}",
                color=discord.Colour.embed_background()
            )
            await channel.send(embed=embed)
        
            
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        channel = await return_channel(self, guild_id=guild.id)
        async for entry in guild.audit_logs(action=discord.AuditLogAction.unban, limit=1):
            embed = discord.Embed(title="👥 USER Unbanned", description=f"**Name:** {user.mention} | `{user}`\n**ID:** `{user.id}`\n**Unbanned from:** {entry.user.mention}", color=discord.Colour.embed_background())
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Log(bot))