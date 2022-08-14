from tech_blog.use_case.Irepos.article import IArticleRepo
from tech_blog.models.article import Article as ArticleModel
from tech_blog.domain.entities.article import Article as ArticleEntity
from tech_blog.use_case.dto.article import GetInputData
import typing as t
from loguru import logger

class ArticleRepo(IArticleRepo):
    def get_articles(filter: GetInputData) -> t.List[ArticleEntity]:
        query = ArticleModel.objects.all()
        total = query.count()
        records = query[filter.offset:filter.offset+filter.limit]
        return [ArticleEntity.build(record) for record in records], total
        