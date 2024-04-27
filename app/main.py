from fastapi import FastAPI

from app.images.router import router_images

app = FastAPI()

app.include_router(router_images)
