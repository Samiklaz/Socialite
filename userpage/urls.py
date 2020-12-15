from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'userpage'

urlpatterns = [
    path('', views.user_home, name='home'),
    path('post', views.post, name='post'),
    path("like_dislike", views.like_post, name='like_dislike_post'),
    path('<int:post_id>', views.delete_post, name='delete_post'),
    path("comment", views.comment, name="comment"),
    path("<str:username>", views.user_profile, name='user_profile'),
    path("user/follow/<str:username>", views.follow, name="follow"),
    path("search/<str:username>", views.Search.as_view(), name="search_user"),

]