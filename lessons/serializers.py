from rest_framework.serializers import ModelSerializer
from .models import Lesson


class LessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'template_id', 'preferences']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
