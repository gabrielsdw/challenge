from .serializers import LessonModelSerializer, LessonUpdateModelSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Lesson


class LessonCreateApiVIew(CreateAPIView):
    serializer_class = LessonModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonUpdateModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()
    
    
    def get_object(self):
        lesson = super().get_object()
        if lesson.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this lesson.")
        return lesson
    