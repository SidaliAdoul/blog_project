from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .models import Post

urlpatterns = [
    path("", BlogListView.as_view(model=Post), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(model=Post), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(model=Post), name="post_new"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(model=Post), name="post_edit"),
    path("post/<int:pk>/delete", BlogDeleteView.as_view(model=Post), name="post_delete")
]