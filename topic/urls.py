from django.urls import path
from .views import TopicListView, TopicDetailView
urlpatterns=[
    path("post/<int:pk>/",TopicDetailView.as_view(),name="post_detail"),
    path("",TopicListView.as_view(), name="home"),
]