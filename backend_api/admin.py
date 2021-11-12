from django.contrib import admin

from backend_api.models import Post, UserFollowing

admin.site.register(Post)
admin.site.register(UserFollowing)