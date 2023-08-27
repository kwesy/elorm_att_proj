from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('create', views.CreateUserView.as_view()),
    path('', views.UpdateUserView.as_view()),
    path('<int:pk>', views.GetUserView.as_view()),
    *router.urls
]