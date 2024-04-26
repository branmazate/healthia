from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r"userqueries", views.UserQueryViewSet)
router.register(r"chatresponse", views.ChatResponseViewSet)

urlpatterns = [
    path("", include(router.urls)), #DRF router url)
    path("register/", views.UserCreate.as_view(), name="register"), #Registration url
    path("login/", obtain_auth_token, name="login"), #DRF login url
    path("logout/", views.Logout.as_view(), name="logout"), #Logout url)
]
