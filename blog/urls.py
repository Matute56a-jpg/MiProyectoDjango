from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("crear/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/editar/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/borrar/", PostDeleteView.as_view(), name="post_delete"),
]
