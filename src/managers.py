from src.models import users, organizations, announcements
from src.db import database

class UserManager:
    @classmethod
    async def all(cls):
        query = users.select()
        return await database.fetch_all(query)
    
    @classmethod
    async def get(cls, id):
        query = users.select().where(users.c.id == id)
        return await database.fetch_one(query)

    @classmethod
    async def create(cls, **data):
        query = users.insert().values(**data)
        return await database.execute(query)
    
    
class OrganizationManager:
    @classmethod
    async def all(cls):
        query = organizations.select()
        return await database.fetch_all(query)
    
    @classmethod
    async def get(cls, id):
        query = organizations.select().where(organizations.c.id == id)
        return await database.fetch_one(query)

    @classmethod
    async def create(cls, **data):
        query = organizations.insert().values(**data)
        return await database.execute(query)
    
    
class AnnouncementManager:
    @classmethod
    async def all(cls):
        query = announcements.select()
        return await database.fetch_all(query)
    
    @classmethod
    async def get(cls, id):
        query = announcements.select().where(announcements.c.id == id)
        return await database.fetch_one(query)

    @classmethod
    async def create(cls, **data):
        query = announcements.insert().values(**data)
        return await database.execute(query)