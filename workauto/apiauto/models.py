from django.db import models
from mdeditor.fields import MDTextField


class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()

    class Meta:
        verbose_name_plural = "Markdown content"

    def __str__(self):
        return self.title

class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()    