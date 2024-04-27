from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ImageTagAssociation(Base):
    __tablename__ = 'image_tag_association'

    id: Mapped[int] = mapped_column(primary_key=True)
    image_id: Mapped[int] = mapped_column(ForeignKey('image.id'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tag.id'))
    value: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return f"ImageTagAssociation(id={self.id})"
