from django.contrib import admin
from django.urls import path
from .views import RegisterUser, UserShow, PostShow, PostDetail, BlogCreateView, BlogUpdate, BlogDelete, BlogList

urlpatterns = [

    path(
        'register/',
        PostShow.as_view(),
        name='home'
    ),

    path(
        'post/<int:pk>/',
        PostDetail.as_view(),
        name='post_detail'
    ),

    path(
        'post/new/',
        BlogCreateView.as_view(),
        name='post_new'
    ),

    path(
        'post/<int:pk>/edit/',
        BlogUpdate.as_view(),
        name='post_edit'
    ),

    path(
        'post/<int:pk>/delete/',
        BlogDelete.as_view(),
        name='post_delete'
    ),

    path(
        '',
        BlogList.as_view(),
        name='homeA'
    )

]
