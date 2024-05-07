from src.models import users, organizations
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
    async def create(cls, **user):
        query = users.insert().values(**user)
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
    async def create(cls, **organization):
        query = organizations.insert().values(**organization)
        return await database.execute(query)
    