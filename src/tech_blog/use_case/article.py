from tech_blog.use_case.dto.article import GetInputData, GetOutputData
from tech_blog.use_case.Iboundary.article import IGetInputBoundary, IGetOutBoundary
from tech_blog.use_case.Irepos.article import IArticleRepo
from tech_blog.infra.repos.article import ArticleRepo
import typing as t
from loguru import logger

class GetArticlesUseCase(IGetInputBoundary):
    repos: IArticleRepo
    boundary: IGetOutBoundary
    
    def __init__(self, presenter: IGetOutBoundary):
        self.repos = ArticleRepo
        self.boundary = presenter
    
    def get_articles(self, filter: GetInputData) -> t.Any:
        entities, total = self.repos.get_articles(filter)
        output_data = GetOutputData.build(entities, total)
        return self.boundary.presenter(output_data)