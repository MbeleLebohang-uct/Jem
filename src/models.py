from sqlalchemy import (
    TIMESTAMP, 
    Boolean, 
    Column, 
    Enum, 
    ForeignKey, 
    String, 
    Uuid, 
    Table, 
    func
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import text

from src.db import metadata


organizations = Table(
    "organizations",
    metadata,
    Column("id", Uuid, primary_key=True, index=True, server_default=text("gen_random_uuid()")),
    Column("name", String, nullable=False),
    Column("created_by", JSONB, nullable=False),
    Column("metadata", JSONB),
    Column("deleted", Boolean, nullable=False, default=False),
    Column("deleted_at", TIMESTAMP(timezone=True)),
    Column("created_at", TIMESTAMP(timezone=True), nullable=False, default=func.current_timestamp()),
    Column("updated_at", TIMESTAMP(timezone=True), nullable=False, onupdate=func.current_timestamp())
)

user_role = Enum("admin", "employee", "employer", name="user_role")

users = Table(
    "users",
    metadata,
    Column("id", Uuid, primary_key=True, index=True),
    Column("email", String, unique=True),
    Column("role", user_role),
    Column("organization_id", Uuid, ForeignKey("organizations.id"), nullable=True),
    Column("metadata", JSONB),
    Column("deleted", Boolean, nullable=False, default=False),
    Column("deleted_at", TIMESTAMP(timezone=True)),
    Column("created_at", TIMESTAMP(timezone=True), nullable=False, default=func.current_timestamp()),
    Column("updated_at", TIMESTAMP(timezone=True), nullable=False, onupdate=func.current_timestamp())
)

messages = Table(
    "messages",
    metadata,
    Column("id", Uuid, primary_key=True, index=True, server_default=text("gen_random_uuid()")),
    Column("body", String, nullable=False),
    Column("owner_id", Uuid, ForeignKey("users.id"), nullable=False),
    Column("metadata", JSONB),
    Column("deleted", Boolean, nullable=False, default=False),
    Column("deleted_at", TIMESTAMP(timezone=True)),
    Column("created_at", TIMESTAMP(timezone=True), nullable=False, default=func.current_timestamp()),
    Column("updated_at", TIMESTAMP(timezone=True), nullable=False, onupdate=func.current_timestamp())
)

announcements = Table(
    "announcements",
    metadata,
    Column("id", Uuid, primary_key=True, index=True, server_default=text("gen_random_uuid()")),
    Column("body", String, nullable=False),
    Column("organization_id", Uuid, ForeignKey("organizations.id"), nullable=False),
    Column("created_by", JSONB, nullable=False),
    Column("publish_at", TIMESTAMP(timezone=True), nullable=False),
    Column("published", Boolean, nullable=False, default=False),
    Column("metadata", JSONB),
    Column("deleted", Boolean, nullable=False, default=False),
    Column("deleted_at", TIMESTAMP(timezone=True)),
    Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp()),
    Column("updated_at", TIMESTAMP(timezone=True), nullable=False, onupdate=func.current_timestamp())
) 
