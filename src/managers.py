from src.models import users, messages, announcements
from src.db import database

class UserManager:
    @classmethod
    async def all(cls, build_query=None):
        query = build_query(users) if build_query else users.select()
        return await database.fetch_all(query)


class AnnouncementManager:
    @classmethod
    async def all(cls, build_query=None):
        query = build_query(announcements) if build_query else announcements.select()
        return await database.fetch_all(query)
    
    @classmethod
    async def create(cls, **data):
        query = announcements.insert().values(**data)
        return await database.execute(query)
    
    
class MessageManager:
    @classmethod
    async def create_batch(cls, data: list):
        query = messages.insert().values(data)
        return await database.execute(query)