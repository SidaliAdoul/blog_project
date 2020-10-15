from django.urls import path
from .views import BlogListView
from .models import Post

urlpatterns = [
    path("", BlogListView.as_view(model=Post), name="home"),
]