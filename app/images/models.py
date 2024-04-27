from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    image_data: Mapped[str]

    def __str__(self):
        return f"Image {self.id}"
