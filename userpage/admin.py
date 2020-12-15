from django.contrib import admin
from .models import Post, Profile, Like, Following


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'image', 'date')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'follower', 'following', 'bio', 'connection', 'user_image')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'likes')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Like)
admin.site.register(Following)
