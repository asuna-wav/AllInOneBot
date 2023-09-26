import ezcord

class JailDatabase(ezcord.DBHandler):
    def __init__(self):
        super().__init__("main.db")
        
    async def setup(self):
        await self.exec("""
            CREATE TABLE IF NOT EXISTS jail (
                guild_id INTEGER,
                user_id INTEGER,
                reason TEXT,
                time INTEGER
            )""")
        await self.exec("""
            CREATE TABLE IF NOT EXISTS jail_role (
                guild_id INTEGER,
                user_id INTEGER,
                role_id INTEGER,
                PRIMARY KEY(guild_id, user_id)
            )""")
        
    async def add(self, guild: int, user: int, time: int):
        await self.exec(
            "INSERT OR IGNORE INTO jail VALUES (?, ?, ?)",
            (guild, user, time),
        )
        time = await self.get_time(guild, user)
        if time is None:
            return True
        else:
            return False
        
        
    async def get_time(self, guild: int, user:int ):
        return await self.one(
            "SELECT time FROM jail WHERE guild_id = ? AND user_id = ?",
            (guild, user),
        )
        
    async def roles(self, guild: int, user: int):
        await self.all(
            "SELECT role_id FROM jail_role WHERE guild_id = ? AND user_id = ?",
            (guild, user),
        )
        