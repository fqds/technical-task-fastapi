from datetime import datetime

from ..db_setup import Base
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)


class Rubrick(Base):
    __tablename__ = "rubrick"

    id = Column(Integer, primary_key=True, index=True)
    bound_post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    name = Column(String)
    post = relationship("Post", back_populates="rubricks")