from django.urls import path
from .views import LessonApiView

urlpatterns = [
    path('lessons/<int:pk>/html-edit/', LessonApiView.as_view(), name='lesson_update'),
]