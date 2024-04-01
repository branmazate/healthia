from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreate, Logout

urlpatterns = [
    path("register/", UserCreate.as_view(), name="register"), #Registration url
    path("login/", obtain_auth_token, name="login"), #DRF login url
    path("logout/", Logout.as_view(), name="logout"), #Logout url)
]
