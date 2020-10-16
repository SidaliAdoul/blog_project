from django.urls import path
from .views import BlogListView,BlogDetailView
from .models import Post

urlpatterns = [
    path("", BlogListView.as_view(model=Post), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(model=Post), name="post_detail"),
]