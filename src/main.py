from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
import pytz
from sqlalchemy import and_, select
from starlette.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from src.db import engine, metadata, database
from src.models import messages
from src.managers import AnnouncementManager, UserManager, MessageManager
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

@scheduler.scheduled_job('interval', seconds=5)
async def publish_announcements():
    now = datetime.now() + timedelta(hours=2) # Timezone workaround
    announcements = await AnnouncementManager.all(lambda model: model.select().where(model.c.publish_at <= now))
        # Get all users in the announcement.org_id who has no message with message.announcement_id == announcement.id
    for announcement in announcements:
        print(f"announcement.id: {announcement.id}")
        users_to_send_messages = await UserManager.all(
            lambda model: model.select()
                .where(
                    and_(
                        model.c.organization_id == announcement.organization_id,
                        ~model.c.id.in_(select(messages.c.owner_id).where(messages.c.announcement_id == announcement.id))
                    )
                )
        )
        
        for user in users_to_send_messages:
            await MessageManager.create(
                created_by={"name":"user", "role":"Admin", "id": "authenticated@user.com"},
                published=False,
                deleted=False,
                updated_at=datetime.now()
            )
            break
                
        print(f"users_to_send_messages: {len(users_to_send_messages)}")
    print(f"scheduled_job_1: {len(announcements)}")
    print(f"scheduled_job_1t: {[x.publish_at for x in announcements]}")

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