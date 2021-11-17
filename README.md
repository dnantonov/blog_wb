
### Endpoints

1. http://127.0.0.1:8000/api/login/  
Authorization of existing users  
Method: POST  
Example:
```json
{
    "username": "username",
    "email": "user@mail.com",
    "password": "password1"
}
```

2. http://127.0.0.1:8000/api/logout/  
Logout for existing users  
Method: POST  

3. http://127.0.0.1:8000/api/register/  
Registration of new users  
Method: POST  
Example:  
```json
{
    "username": "username",
    "email": "user@mail.com",
    "password1": "password1",
    "password2": "password1"
}
```

4. http://127.0.0.1:8000/api/create_post/  
Creating a new post for an authorized user  
Method: POST
Example:
```json
{
    "title": "Title Text",
    "body": "Body Text"
}
```

5. http://127.0.0.1:8000/api/users/  
Getting a list of all users sorted by the number of posts  
Method: GET

6. http://127.0.0.1:8000/api/posts/  
Getting all posts with the exception of the posts of the current user and the ability to sort by publication date  
Method: GET

7. http://127.0.0.1:8000/api/follow/{str:username}/  
Following to another user by username  
Method: GET
Parameter: username
Example: http://127.0.0.1:8000/api/follow/username/

8. http://127.0.0.1:8000/api/unfollow/{str:username}/ 
Unfollowing to another user by username
Method: GET
Parameter: username
Example: http://127.0.0.1:8000/api/unfollow/username/

9. http://127.0.0.1:8000/api/feed/  
News feed from the posts of the users on which the subscription was carried out. Sort by post creation date. The list of posts is given in pages of 10 pieces  
Method: GET

10. http://127.0.0.1:8000/api/posts/{int:pk}/  
Marking a post as read  
Method: GET
Parameter: pk
Example: http://127.0.0.1:8000/api/posts/1/

