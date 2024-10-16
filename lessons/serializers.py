from rest_framework.serializers import ModelSerializer
from .models import Lesson


class LessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'html_content']

    """
    def validate_title(self, data):
        ...
    """
    """
    def validate_html_content(self, data):
        html_content    
    """