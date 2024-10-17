from django.urls import path
from .views import TemplateListApiView

urlpatterns = [
    path('templates/', TemplateListApiView.as_view(), name='template_list'),
]
