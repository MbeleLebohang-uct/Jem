from contextlib import asynccontextmanager
from datetime import datetime
from fastapi import FastAPI, HTTPException
import pytz
from starlette.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from src.db import engine, metadata, database
from src.jobs import create_user_messages
from src.managers import AnnouncementManager, UserManager
from src.schema import AnnouncementInput, UserModel

metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

jobstores = {
    'default': MemoryJobStore()
}

scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Africa/Johannesburg') 

@scheduler.scheduled_job('interval', seconds=6)
async def create_user_messages_job():
    await create_user_messages()
    
                
@asynccontextmanager
async def lifespan(app: FastAPI):
    print('--------- startup -----------')
    await database.connect()
    yield
    print('--------- shutdown -----------')
    await database.disconnect()
    scheduler.shutdown()

app.router.lifespan_context = lifespan
scheduler.start()


@app.get("/")
async def read_root():
    users = await UserManager.all()
    return [UserModel(**user).model_dump() for user in users]

@app.post("/announcement/")
async def create_announcement(announcement: AnnouncementInput):
    data = announcement.model_dump()
    try:
        await AnnouncementManager.create(
            **data, 
            created_by={"name":"user", "role":"Admin", "id": "authenticated@user.com"},
            published=False,
            deleted=False,
            updated_at=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Announcement created successfully"}