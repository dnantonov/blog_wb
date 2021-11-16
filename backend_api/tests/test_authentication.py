from django.urls import reverse

from rest_framework.test import APITestCase


class BaseTest(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = {
            'username': 'test_username',
            'email': 'test@testmail.com',
            'password1': 'test_password',
            'password2': 'test_password'
        }
        self.user_short_password = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password1': 'tes',
            'password2': 'tes',
        }
        self.user_unmatching_password = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password1': 'teslatt',
            'password2': 'teslatto'
        }
        self.user_invalid_email = {
            'email': 'test.com',
            'username': 'username',
            'password1': 'teslatt',
            'password2': 'teslatto'
        }
        self.login_user = {
            'username': 'test_username',
            'email': 'test@testmail.com',
            'password': 'test_password'
        }
        return super().setUp()


class RegisterTest(BaseTest):
    def test_register(self):
        response = self.client.post(self.register_url, self.user, format='json')
        self.assertEqual(response.status_code, 201)

    def test_register_user_withshortpassword(self):
        response = self.client.post(self.register_url, self.user_short_password, format='json')
        self.assertEqual(response.status_code, 400)

    def test_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url, self.user_unmatching_password, format='json')
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(self.register_url, self.user_invalid_email, format='json')
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_taken_email(self):
        self.client.post(self.register_url, self.user, format='json')
        response = self.client.post(self.register_url, self.user, format='json')
        self.assertEqual(response.status_code, 400)


class LoginTest(BaseTest):
    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='json')
        response = self.client.post(self.login_url, self.login_user, format='json')
        self.assertEqual(response.status_code, 200)

    def test_cant_login_with_no_username(self):
        login_data = {'username': '', 'email': 'email', 'password': 'passwped'}
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_cant_login_with_no_password(self):
        login_data = {'username': 'username', 'email': 'email', 'password': ''}
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, 400)


class LogoutTest(BaseTest):
    def test_logout_success(self):
        self.client.post(self.login_url, self.login_user, format='json')
        response = self.client.post(self.logout_url, format='json')
        self.assertEqual(response.status_code, 200)


class CreatePostTest(BaseTest):
    pass


class UsersListTest(BaseTest):
    pass


class PostsListTest(BaseTest):
    pass


class FollowersTest(BaseTest):
    pass


class FeedTest(BaseTest):
    pass


class ReadPostTest(BaseTest):
    pass

