from app.core.models import BaseModel

from sqlalchemy import DateTime, String, ForeignKey, Boolean
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from uuid import uuid4



class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True, 
        default=lambda: str(uuid4()),
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(36), )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
    )

    tokens = relationship("Token", back_populates="user")


class Token(BaseModel):
    __tablename__ = 'tokens'

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, 
        default=lambda: str(uuid4()),
        index=True
    )
    user_id: Mapped[str] = mapped_column(
        String(36), 
        ForeignKey("users.id"),
        index=True,
    )
    token_hash: Mapped[str] = mapped_column(String(64), unique=True)
    revoked: Mapped[bool] = mapped_column(Boolean, default=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
    )
