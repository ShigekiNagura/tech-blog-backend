from __future__ import annotations
import typing as t
from pydantic import BaseModel
from tech_blog.use_case.dto.article import GetOutputData, ArticleData

class ArticleDataVM(BaseModel):
    id: int
    title: str
    updated_at: str
    
    @classmethod
    def build(cls, tmp: ArticleData) -> ArticleDataVM:
        return cls(**{
            "id": tmp.id,
            "title": tmp.title,
            "updated_at": tmp.updated_at.strftime('%Y-%m-%d')
        })
    
class GetArticlesVM(BaseModel):
    total: int
    data: t.List[ArticleDataVM]
    
    @classmethod
    def build(cls, data: GetOutputData):
        return cls(**{
            "total": len(data.data),
            "data": [ArticleDataVM.build(tmp) for tmp in data.data]
        })
    