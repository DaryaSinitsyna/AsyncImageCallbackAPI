from app.dao.base import BaseDAO
from app.image_tag_association.dao import ImageTagDAO
from app.image_tag_association.models import ImageTagAssociation
from app.images.models import Image
from app.tags.dao import TagDAO
from app.tags.helpers import get_image_tags


class ImageDAO(BaseDAO):
    model = Image

    @classmethod
    async def insert_image_tags(cls, contents, base64_data):
        image = await ImageDAO.add(image_data=base64_data)
        tags, values = await get_image_tags(image_data=contents)
        current_tags = await TagDAO.add_many(tags)
        image_tags = [ImageTagAssociation(image_id=image.id, tag_id=current_tags[index], value=values[index]) for index in range(len(current_tags))]
        await ImageTagDAO.add_all(image_tags)
