from django.contrib.auth.models import User
from django.db.models import Count

import django_filters.rest_framework
from rest_framework import status, filters, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend_api.models import Post, UserFollowing
from backend_api.serializers import PostSerializer, UserSerializer


class CreatePostView(CreateAPIView):
    """
    Class Based View for create a post by authenticated user.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={'request': request})
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class PostsListView(viewsets.ModelViewSet):
    """
    Get all posts except posts current user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_date']
    ordering = ['-published_date']
    
    def get_queryset(self):
        return Post.objects.all().exclude(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class.data)


class UsersListView(viewsets.ModelViewSet):
    """
    Get all users and count posts by each user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all().annotate(posts_count=Count('post'))
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('posts_count',)
    
    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class.data)


class UserFollowingView(APIView):
    """
    View for following user by username.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, username, *args, **kwargs):
        current_user = request.user
        follow_user = User.objects.get(username=username)
        UserFollowing.objects.create(user_id=current_user,
                                     following_user_id=follow_user)
        data = {
            'success': 'ok',
            'info': f'You are following {follow_user}'
        }
        return Response(data)


class UserUnfollowingView(UserFollowingView):
    """
    View for unfollow user by username.
    """
    def get(self, request, username, *args, **kwargs):
        current_user = request.user
        unfollow_user = User.objects.get(username=username)
        UserFollowing.objects.filter(user_id=current_user,
                                     following_user_id=unfollow_user).delete()
        data = {
            'success': 'ok',
            'info': f'You unfollowed {unfollow_user}'
        }
        return Response(data)


class FeedView(PostsListView):
    def get_queryset(self):
        qs = UserFollowing.objects.filter(user_id=self.request.user.id)
        following_ids = [q.following_user_id.id for q in qs]
        return Post.objects.filter(owner__id__in=following_ids).exclude(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class.data)



