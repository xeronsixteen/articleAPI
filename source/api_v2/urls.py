from django.urls import path

from api_v2.views import ArticleView

from source.api_v2.views import DetailView

app_name = "api_v2"

urlpatterns = [
    path("articles/", ArticleView.as_view()),
    path("articles/<int:pk>/", ArticleView.as_view()),
    path("article/<int:pk>/", DetailView.as_view()),


]
