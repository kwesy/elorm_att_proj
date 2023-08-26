from django.urls import path
from . import views 


urlpatterns = [
    path('attendances/', views.ListCreateAttendanceView.as_view()),
    path('attendances/record/<int:finger_id>', views.ListCreateAttendanceView.as_view()),
]