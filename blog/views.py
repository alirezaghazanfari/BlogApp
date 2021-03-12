from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import View,APIView
from rest_framework import viewsets, permissions
from django.views.generic import ListView , DetailView

from blog.models.Post import User,Post
# Create your views here.

class RegisterUser(ListView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_register.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserShow(ListView):
    model = User
    template_name = ''
class PostShow(ListView):
    model = Post
    template_name = 'posts_show.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


