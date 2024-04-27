import base64
from fastapi import APIRouter, UploadFile, Depends

from app.image_tag_association.dao import ImageTagDAO
from app.images.auth import get_api_key
from app.images.dao import ImageDAO
from app.images.helpers import get_words_from_text, send_request
from app.images.schemas import SRequestData, SImageBase64

router_images = APIRouter(
    prefix="/images",
    tags=["Images"],
)


@router_images.post("/upload", status_code=201)
async def upload_image(file: UploadFile, api_key: str = Depends(get_api_key)):
    contents = await file.read()
    base64_data = base64.b64encode(contents).decode('utf-8')
    await ImageDAO.insert_image_tags(contents, base64_data)
    return {"message": "File downloaded"}


callback_router = APIRouter()


@callback_router.post(
    "{$callback_url}", status_code=200)
def get_image(request_data: SImageBase64):
    pass


@router_images.post("/tags", callbacks=callback_router.routes)
async def image_by_tags(request_data: SRequestData, api_key: str = Depends(get_api_key)):
    words = await get_words_from_text(request_data.text_query)
    callback_url = request_data.callback_url
    image_id, image_data = await ImageTagDAO.select_image(words)
    callback_data = {"result": image_data}
    await send_request(callback_url, callback_data)
    return {"image_id": image_id, "image_data": image_data}
