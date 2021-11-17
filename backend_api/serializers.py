from rest_framework import serializers

from backend_api.models import Post, UserFollowing

from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

User = get_user_model()


class CustomTokenCreateSerializer(TokenCreateSerializer):
    """
    Serializer for authenticate users.
    """
    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user:
            return attrs
        self.fail("invalid_credentials")


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts in blog.
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = ('title', 'body', 'owner', 'published_date', 'read')


class FollowingSerializer(serializers.ModelSerializer):
    """
    Serializer for follow users.
    """
    class Meta:
        model = UserFollowing
        fields = ("id", "following_user_id", "created")
        

class FollowersSerializer(serializers.ModelSerializer):
    """
    Serializer for unfollow users.
    """
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for manage account info.
    """
    posts_count = serializers.IntegerField(read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'posts_count', "following", "followers")
        extra_kwargs = {"password": {"write_only": True}}

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data


