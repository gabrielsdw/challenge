from django.db import models
from django.contrib.auth import get_user_model


class Lesson(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    html_content = models.TextField()

    def __str__(self):
        return self.title