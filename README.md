
### Endpoints

1. http://127.0.0.1:8000/api/login/  
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
Method: POST


3. http://127.0.0.1:8000/api/register/  
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
Method: POST
Example:
```json
{
    {
    "title": "Title Text",
    "body": "Body Text"
}
}
```

5. http://127.0.0.1:8000/api/users/  
Method: GET

6. http://127.0.0.1:8000/api/posts/  
Method: GET

7. http://127.0.0.1:8000/api/follow/{str:username}/  
Method: GET
Parameter: username
Example: http://127.0.0.1:8000/api/follow/username/

8. http://127.0.0.1:8000/api/unfollow/{str:username}/ 
Method: GET
Parameter: username
Example: http://127.0.0.1:8000/api/unfollow/username/

9. http://127.0.0.1:8000/api/feed/  
Method: GET

10. http://127.0.0.1:8000/api/posts/{int:pk}/  
Method: GET
Parameter: pk
Example: http://127.0.0.1:8000/api/posts/1/

