from django.urls import path, include
from django.contrib import admin
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('api/', include('backend_api.urls'))
]
