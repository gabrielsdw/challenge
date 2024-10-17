from django.urls import path
from .views import LessonUpdateApiView, LessonCreateApiView, LessonRetriveApiView

urlpatterns = [
    path('lessons/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', LessonRetriveApiView.as_view(), name='lesson_retrive'),
    path('lessons/<int:pk>/html-edit/', LessonUpdateApiView.as_view(), name='lesson_update'),
]



