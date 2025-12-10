from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

@register_snippet
class ScriptureComparison(models.Model):
    book_title = models.CharField(max_length=100)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    kjv_text = models.TextField(verbose_name="King James Version", blank=True)
    ethiopian_text = models.TextField(verbose_name="Ethiopian/Gnostic Text")
    analysis = models.TextField(blank=True, help_text="Ministry reflection on the difference")
    panels = [
        FieldPanel('book_title'),
        FieldPanel('chapter'),
        FieldPanel('verse'),
        FieldPanel('kjv_text'),
        FieldPanel('ethiopian_text'),
        FieldPanel('analysis'),
    ]

    class Meta:
        ordering = ['book_title', 'chapter', 'verse']

    def __str__(self):
        return f"{self.book_title} {self.chapter}:{self.verse}"