from django.urls import reverse

from rest_framework.test import APITestCase

from backend_api.models import Post, User
from backend_api.serializers import PostSerializer, UserSerializer


class BaseTest(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.create_post_url = reverse('create-post')
        self.posts_url = reverse('posts')
        self.users_url = reverse('users')
        self.user = {
            'username': 'test_username',
            'email': 'test@testmail.com',
            'password1': 'test_password',
            'password2': 'test_password'
        }
        self.user2 = {
            'username': 'test_username2',
            'email': 'test2@testmail.com',
            'password1': 'test_password2',
            'password2': 'test_password2'
        }
        self.login_user = {
            'username': 'test_username',
            'email': 'test@testmail.com',
            'password': 'test_password'
        }
        self.login_user2 = {
            'username': 'test_username2',
            'email': 'test2@testmail.com',
            'password': 'test_password2'
        }
        self.post = {
            "title": "Test title text",
            "body": "Test body text."
        }
        self.client.post(self.register_url, self.user, format='json')
        self.client.post(self.register_url, self.user2, format='json')
        return super().setUp()
    

class CreatePostTest(BaseTest):
    def test_create_post_not_authenticated(self):
        response = self.client.post(self.create_post_url, self.post, format='json')
        self.assertEqual(response.status_code, 401)
    
    def test_create_post_successfully(self):
        self.client.post(self.login_url, self.login_user, format='json')
        response = self.client.post(self.create_post_url, self.post, format='json')
        self.assertEqual(response.status_code, 200)
        
    def test_check_post_exists(self):
        self.client.post(self.login_url, self.login_user, format='json')
        self.client.post(self.create_post_url, self.post, format='json')
        post = Post.objects.filter(title=self.post['title']).first()
        self.assertIsNotNone(post)


class PostsListTest(BaseTest):
    def test_posts_not_authenticated(self):
        response = self.client.get(self.posts_url, format='json')
        self.assertEqual(response.status_code, 401)
        
    def test_current_user_posts_are_not_displayed(self):
        self.client.post(self.login_url, self.login_user, format='json')
        self.client.post(self.create_post_url, {"title": "test title1", "body": "test body1"}, format='json')
        posts = Post.objects.all()
        serializer_data = PostSerializer(posts, many=True).data
        response = self.client.get(self.posts_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(serializer_data, response.data)
    
    def test_other_users_posts_are_displayed_and_correct_ordering(self):
        self.client.post(self.login_url, self.login_user, format='json')
        user = User.objects.get(username="test_username2")
        Post.objects.create(title='test title1', body='test body1', owner=user)
        Post.objects.create(title='test title2', body='test body2', owner=user)
        posts = Post.objects.all()
        serializer_data = PostSerializer(posts, many=True).data
        response = self.client.get(self.posts_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer_data[::-1], response.data['results'])
        self.assertEqual(serializer_data[0]['title'], 'test title1')


class UsersListTest(BaseTest):
    def test_users_list_not_authenticated(self):
        response = self.client.get(self.users_url, format='json')
        self.assertEqual(response.status_code, 401)
    
    def test_users_ordering(self):
        self.client.post(self.login_url, self.login_user, format='json')
        user = User.objects.get(username="test_username2")
        Post.objects.create(title='test title1', body='test body1', owner=user)
        Post.objects.create(title='test title2', body='test body2', owner=user)
        response = self.client.get(self.users_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['posts_count'], 0)
        self.assertEqual(response.data['results'][1]['posts_count'], 2)


class FollowersTest(BaseTest):
    pass


class FeedTest(BaseTest):
    pass


class ReadPostTest(BaseTest):
    pass