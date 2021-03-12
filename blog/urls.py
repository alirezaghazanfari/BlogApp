from django.contrib import admin
from django.urls import path
from .views import RegisterUser,UserShow,PostShow,PostDetail

urlpatterns = [
    path('register/',PostShow.as_view(),name='home'),
    path('post/<int:pk>/',PostDetail.as_view(),name = 'post_detail'),
]
