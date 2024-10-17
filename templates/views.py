from rest_framework.generics import ListAPIView
from .serializers import TemplateModelSerializer
from .models import Template


class TemplateListApiView(ListAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateModelSerializer
