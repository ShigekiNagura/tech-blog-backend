from django.urls import path

from tech_blog.view.article import ArticleView

urlpatterns = [
    path("articles", ArticleView.as_view())
]
