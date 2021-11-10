from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

from backend_api.views import CreatePostView, ListPosts


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('create_post/', CreatePostView.as_view()),
    path('list_posts/', ListPosts.as_view()),
]
