from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreate, Logout, UserQueryViewSet, ChatResponseViewSet

router = DefaultRouter()
router.register(r"userquery", UserQueryViewSet)
router.register(r"chatresponse", ChatResponseViewSet)

urlpatterns = [
    path("", include(router.urls)), #DRF router url)
    path("register/", UserCreate.as_view(), name="register"), #Registration url
    path("login/", obtain_auth_token, name="login"), #DRF login url
    path("logout/", Logout.as_view(), name="logout"), #Logout url)
]
