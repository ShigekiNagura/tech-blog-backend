from tech_blog.utils.exception_handler import handle_except
from rest_framework.views import APIView
from rest_framework.response import Response
from tech_blog.use_case.dto.article import GetInputData
from tech_blog.use_case.Iboundary.article import IGetInputBoundary
from tech_blog.view.presenter.article import GetArticlesPresenter
from tech_blog.use_case.article import GetArticlesUseCase

class ArticleView(APIView):
    def get(self, request, format=None):
        params = {
            "offset": int(request.query_params["offset"]),
            "limit": int(request.query_params["limit"])
        }
        with handle_except():
            filter = GetInputData(**params)
            p = GetArticlesPresenter()
            uc: IGetInputBoundary = GetArticlesUseCase(p)
            ret = uc.get_articles(filter)
            return Response(ret.dict())