from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.tags.models import Tag


class TagDAO(BaseDAO):
    model = Tag

    @classmethod
    async def add_many(cls, tags: list[Tag]):
        async with async_session_maker() as session:
            current_tags = []
            for tag in tags:
                current_tag = await cls.add(name=tag.name)
                if not current_tag:
                    current_tag = await cls.find(name=tag.name)
                current_tags.append(current_tag.id)
            await session.commit()
            return current_tags
