from django.db import models
from core.utils import search_element_ids_template


class Template(models.Model):
    name = models.CharField(max_length=200)
    html_content = models.TextField()
    html_element_keys =  models.JSONField(default=list, blank=True)

    def save(self, *args, **kwargs):
        self.html_element_keys = search_element_ids_template(template=self.html_content)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Template - {self.name}"
    
