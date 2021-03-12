from rest_framework import serializers
from blog.models.Post import User,Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','last_name','ip']
