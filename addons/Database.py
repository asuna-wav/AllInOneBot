import ezcord



class DBChannel(ezcord.DBHandler):
    def __init__(self):
        super().__init__("main.db")
        
    async def setup(self):
        await self.exec(
            """CREATE TABLE IF NOT EXISTS channels (
                guild_id INTEGER PRIMARY KEY,
                boost_channel INTEGER,
                welcome_channel INTEGER,
                log_channel INTEGER,
                error_channel INTEGER
            )
            """
        )

    async def check(self, guild_id: int):
        await self.exec(
            "INSERT OR IGNORE INTO channels VALUES (?, ?, ?, ?, ?)",
            (guild_id, 0, 0, 0, 0)
        )
        
    async def get(self, guild_id: int, channel: str):
        return await self.one(
            f"SELECT {channel}_channel FROM channels WHERE guild_id = {guild_id}"
        )
    
    async def set(self, channel: str, id: int, guild: int):
        await self.exec(
            f"UPDATE channels SET {channel}_channel = {id} WHERE guild_id = {guild}"
        )
