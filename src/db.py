import os

from sqlalchemy import MetaData, create_engine
from dotenv import load_dotenv
from databases import Database

load_dotenv()
# Database url if none is passed the default one is used
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jem:root1234@localhost/jem")

# SQLAlchemy
metadata = MetaData()
engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)