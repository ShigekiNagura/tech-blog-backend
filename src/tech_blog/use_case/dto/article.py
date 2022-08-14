from __future__ import annotations
from datetime import datetime
import typing as t
from pydantic import BaseModel
from tech_blog.domain.entities.article import Article as ArticleEntity

class GetInputData(BaseModel):
    offset: int
    limit: int


class ArticleData(BaseModel):
    id: int
    title: str
    updated_at: datetime
    
    @classmethod
    def build(cls, entity: ArticleEntity):
        return cls(**{
            "id": entity.id,
            "title": entity.title,
            "updated_at": entity.updated_at
        })

class GetOutputData(BaseModel):
    total: int
    data: t.List[ArticleData]
    
    @classmethod
    def build(cls, entities: t.List[ArticleEntity], total):
        return cls(**{
            "total": total,
            "data": [ArticleData.build(entity) for entity in entities]
        })