import abc
from tech_blog.use_case.dto.article import GetInputData, GetOutputData
from tech_blog.view.view_model.article import GetArticlesVM
import typing as t

class IGetInputBoundary(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_articles(self, filter: GetInputData) -> t.Any:
        pass
    
class IGetOutBoundary(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def presenter(self, data: GetOutputData) -> GetArticlesVM:
        pass
        