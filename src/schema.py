from pydantic import BaseModel, UUID4


class User(BaseModel):
    id: UUID4
    email: str
    
    class Config:
        from_attributes = True