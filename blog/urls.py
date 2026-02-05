from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),      # alias
    path("", views.PostList.as_view(), name="blog_home"), # optional keep both
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]


