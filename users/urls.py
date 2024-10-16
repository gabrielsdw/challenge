from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
]  