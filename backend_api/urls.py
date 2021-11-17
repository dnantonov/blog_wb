from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView

from backend_api.views import CreatePostView, PostsListView, UsersListView,\
                              UserFollowingView, UserUnfollowingView, FeedView, \
                              ReadPostView


urlpatterns = [
    # Authentication urls
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
#     path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
#     path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
#     path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
#     re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),

    # Blog urls
    path('create_post/', CreatePostView.as_view(), name='create-post'),
    path('posts/', PostsListView.as_view({'get': 'list'}), name='posts'),
    path('users/', UsersListView.as_view({'get': 'list'}), name='users'),
    path('follow/<str:username>/', UserFollowingView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UserUnfollowingView.as_view(), name='unfollow'),
    path('feed/', FeedView.as_view({'get': 'list'}), name='feed'),
    path('posts/<int:pk>/', ReadPostView.as_view(), name='post'),
]
