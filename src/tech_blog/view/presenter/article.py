from tech_blog.use_case.dto.article import GetOutputData
from tech_blog.view.view_model.article import GetArticlesVM
from tech_blog.use_case.Iboundary.article import IGetOutBoundary

class GetArticlesPresenter(IGetOutBoundary):
    def presenter(self, data: GetOutputData) -> GetArticlesVM:
        return GetArticlesVM.build(data)