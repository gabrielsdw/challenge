from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Lesson
from templates.models import Template
from django.shortcuts import get_object_or_404


def validate_preference(value, template_id):
    template = get_object_or_404(Template, pk=template_id)
    
    keys = list(value.keys()) if value else None
    keys_to_remove = []

    if keys:
        for key in keys:
            if key not in list(template.html_element_keys):
                keys_to_remove.append(key)
                continue

            dict = value.get(key)

            if 'value' in dict.keys() and 'property' in dict.keys():
                continue
            else:
                raise ValidationError(
                    """The preference format -> "preferences": { "element_key_existing_on_template": {"property": "property", "value": "value"}}"""
                )
    
    for key in keys_to_remove:
        del value[key]
    return value


class LessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'template_id', 'preferences']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    def validate_preferences(self, value):
        template_id = self.instance.template_id
        return validate_preference(value, template_id)


class LessonUpdateModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['preferences']

    def validate_preferences(self, value):
        template_id = self.instance.template_id
        return validate_preference(value, template_id)
