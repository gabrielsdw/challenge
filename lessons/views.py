from .serializers import LessonModelSerializer, LessonUpdateModelSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnlyLesson
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Lesson


class LessonRetriveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer


class LessonListCreateApiView(ListCreateAPIView):
    serializer_class = LessonModelSerializer
    queryset = Lesson.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Lesson.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset 



class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonUpdateModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyLesson]
    queryset = Lesson.objects.all()
