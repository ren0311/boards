from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, TagCreateView
from . import views

app_name = "memorandum"
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.ArticleListView.as_view(), name="index"),
    path("create/", views.ArticleCreateView.as_view(), name="create"),
    path("article/<int:pk>/", views.ArticleDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.ArticleUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ArticleDeleteView.as_view(), name="delete"),
    path("tag/create/", views.TagCreateView.as_view(), name="create_tag"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("tag/create/", TagCreateView.as_view(), name="create_tag"),
]
