from django.contrib import admin
from blog.models.Post import Post,User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('name','last_name')
    #readonly_fields = ('name','last_name','ip')
    list_display = ('last_name','name','ip')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title','body','author')
    #readonly_fields = ('title','body','user')
    list_display = ('title','author')