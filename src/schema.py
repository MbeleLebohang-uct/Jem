from pydantic import BaseModel, UUID4, field_validator
from datetime import datetime


class UserModel(BaseModel):
    id: UUID4
    email: str
    
    class Config:
        from_attributes = True
        
        
class AnnouncementInput(BaseModel):
    body: str
    organization_id: str
    publish_at: datetime
    
    class Config:
        from_attributes = True
        
    @field_validator("publish_at", mode='after')
    def convert_timezone(cls, value):
        return value.replace(tzinfo=None)