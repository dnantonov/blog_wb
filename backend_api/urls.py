from django.urls import path

from backend_api.views import CreatePostView, ListPosts

urlpatterns = [
    path('create_post/', CreatePostView.as_view()),
    path('list_posts/', ListPosts.as_view()),
]
