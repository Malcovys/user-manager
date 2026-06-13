from app.core.models import BaseModel

from uuid import uuid4

from sqlalchemy import func
from sqlalchemy import String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import mapped_column, Mapped



class Log(BaseModel):
    __tablename__ = "logs"

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