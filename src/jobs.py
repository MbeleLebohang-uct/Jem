from datetime import datetime, timedelta

from sqlalchemy import and_, select

from src.managers import AnnouncementManager, UserManager, MessageManager
from src.models import messages

def _build_message_data(announcement, user):
    return {
        "body": announcement.body, 
        "owner_id": user.id, 
        "announcement_id": announcement.id, 
        "deleted": False, 
        "updated_at": datetime.now()
    }

async def create_user_messages():
    now = datetime.now() + timedelta(hours=2) # Timezone workaround
    announcements = await AnnouncementManager.all(lambda model: model.select().where(
            and_(
                model.c.publish_at <= now, 
                model.c.published == False
            )
        )
    )
    
    for announcement in announcements:
        users_to_send_messages = await UserManager.all(
            lambda model: model.select()
                .where(
                    and_(
                        model.c.organization_id == announcement.organization_id,
                        ~model.c.id.in_(select(messages.c.owner_id).where(messages.c.announcement_id == announcement.id))
                    )
                )
        )
        
        if len(users_to_send_messages) == 0:
            await AnnouncementManager.update(id=announcement.id, published=True)
            continue
        
        await MessageManager.create_batch([_build_message_data(announcement, user) for user in users_to_send_messages])
