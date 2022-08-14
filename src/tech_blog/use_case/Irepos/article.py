import abc
from tech_blog.use_case.dto.article import GetInputData
from tech_blog.domain.entities.article import Article
import typing as t

class IArticleRepo(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_articles(filter: GetInputData) -> t.List[Article]:
        pass