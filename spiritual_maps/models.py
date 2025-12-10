from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

@register_snippet
class SpiritualSite(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Concise textual context for the site")
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='sites/', blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('latitude'),
        FieldPanel('longitude'),
        FieldPanel('photo'),
    ]

    def __str__(self):
        return self.name