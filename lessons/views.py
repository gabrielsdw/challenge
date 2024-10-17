from django.shortcuts import get_object_or_404
from .serializers import LessonModelSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Lesson

class LessonCreateApiVIew(CreateAPIView):
    serializer_class = LessonModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class LessonUpdateApiView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    