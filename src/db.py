import os

from sqlalchemy import MetaData, create_engine
from dotenv import load_dotenv
from databases import Database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env"))
DATABASE_URL=os.environ["DATABASE_URL"]

metadata = MetaData()
engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)