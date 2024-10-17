from django.db import models
from templates.models import Template
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from core.utils import fill_template_with_user_preferences


class Lesson(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    template_id  = models.IntegerField()
    html_content = models.TextField(null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True, null=True)

    def save(self, *args, **kwargs):
        content = fill_template_with_user_preferences(self.preferences, get_object_or_404(Template, pk=self.template_id).html_content)
        if content is not None:
            self.html_content = content
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    