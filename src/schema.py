from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    
    class Config:
        from_attributes = True