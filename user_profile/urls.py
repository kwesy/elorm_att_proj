from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateUserView.as_view()),
    path('', views.UpdateUserView.as_view()),
    path('<int:pk>', views.GetUserView.as_view()),
]