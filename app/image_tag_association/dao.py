from fastapi import HTTPException
from sqlalchemy import select, func, desc

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.image_tag_association.models import ImageTagAssociation
from app.images.models import Image
from app.tags.models import Tag


class ImageTagDAO(BaseDAO):
    model = ImageTagAssociation

    @classmethod
    async def add_all(cls, image_tags: list[ImageTagAssociation]):
        async with async_session_maker() as session:
            session.add_all(image_tags)
            await session.commit()

    @classmethod
    async def select_image(cls, words):
        '''
        SELECT ita.image_id, sum(ita.value) as sum_value
        FROM image_tag_association ita
        INNER JOIN tag t on t.id = ita.tag_id
        WHERE t.name in ('car', 'road')
        GROUP BY image_id
        ORDER BY sum_value DESC
        '''
        async with async_session_maker() as session:
            query = (
                select(
                    cls.model.image_id, Image.image_data,
                    func.sum(cls.model.value).label('sum_value')
                )
                    .join(Tag, cls.model.tag_id == Tag.id)
                    .join(Image, cls.model.image_id == Image.id)
                    .where(Tag.name.in_({*words}))
                    .group_by(cls.model.image_id)
                    .order_by(desc('sum_value'))
                    .limit(1)
            )
            result = await session.execute(query)
            query_data = result.mappings().all()
            if not query_data:
                raise HTTPException(status_code=404, detail="Picture is not found")
            data = query_data[0]
            image_id, image_data = data["image_id"], data["image_data"]
            return image_id, image_data
