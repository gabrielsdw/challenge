from django.urls import path
from .views import LessonUpdateApiView, LessonCreateApiVIew

urlpatterns = [
    path('lessons/', LessonCreateApiVIew.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/html-edit/', LessonUpdateApiView.as_view(), name='lesson_update'),
]



