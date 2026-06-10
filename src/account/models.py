from src.core.models import BaseModel

from sqlalchemy import func
from sqlalchemy import DateTime, String, ForeignKey, JSON
from sqlalchemy.orm import  Mapped, mapped_column

from uuid import uuid4



class UserModel(BaseModel):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class UserToken(BaseModel):
    __tablename__ = 'users_tokens'

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))

    token_hash: Mapped[str] = mapped_column(String(64), unique=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class UserLog(BaseModel):
    __tablename__ = "user_logs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("users.id"), nullable=True)

    method: Mapped[str] = mapped_column(String(10)) # GET/POST etc
    path: Mapped[str] = mapped_column(String(255)) # Endpoint

    status_code: Mapped[int] = mapped_column() # 200/400 etc

    ip_address: Mapped[str] = mapped_column(String(50))

    user_agent: Mapped[str] = mapped_column(String(255))

    metadata: Mapped[dict] = mapped_column(JSON)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )