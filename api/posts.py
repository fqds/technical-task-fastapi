from db.models.post import Post

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
router = fastapi.APIRouter()


@router.get("/posts")#, response_model=List[Post])
async def read_users(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


# @router.post("/users", response_model=User, status_code=201)
# async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db=db, email=user.email)
#     if db_user:
#         raise HTTPException(
#             status_code=400, detail="Email is already registered"
#         )
#     return create_user(db=db, user=user)


# @router.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
#     db_user = await get_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.get("/users/{user_id}/courses", response_model=List[Course])
# async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
#     courses = get_user_courses(user_id=user_id, db=db)
#     return 