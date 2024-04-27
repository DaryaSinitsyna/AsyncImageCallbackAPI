from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, sqlite_on_conflict_unique='IGNORE')

    def __str__(self):
        return f"Tag {self.id}"
