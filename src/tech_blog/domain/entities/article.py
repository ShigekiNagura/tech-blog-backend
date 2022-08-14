from __future__ import annotations
from datetime import datetime
import typing as t
from pydantic import BaseModel
from tech_blog.models import Article

class Article(BaseModel):
    id: int
    title: str
    description: str
    topics: t.List[int]
    updated_at: datetime
    
    @classmethod
    def build(cls, record: Article):
        return cls(**{
            "id": record.id,
            "title": record.title,
            "description": record.description,
            "topics": [1, 3],
            "updated_at": record.updated_at
        })