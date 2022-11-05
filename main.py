from fastapi import FastAPI

from db.db_setup import engine
from db.models import post
from api import posts

post.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)