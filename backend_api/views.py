from django.contrib.auth.models import User
from django.db.models import Count

import django_filters.rest_framework
from rest_framework import status, filters, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from backend_api.models import Post, UserFollowing
from backend_api.serializers import PostSerializer, UserSerializer


class CreatePostView(CreateAPIView):
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


class ListPosts(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_date',]
    ordering = ['-published_date']
    
    def get_queryset(self):
        return Post.objects.all().exclude(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class.data)


class UsersListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all().annotate(posts_count=Count('post'))
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('posts_count',)
    
    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class.data)
    
    

