from django.db import models
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

# 1. The Weekly Video (Registered as a Snippet for easy management)
@register_snippet

class WeeklyVideo(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField(help_text="YouTube or Vimeo link")
    is_active = models.BooleanField(default=False, help_text="Check this to display on homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('video_url'),
        FieldPanel('is_active'),
    ]

    def save(self, *args, **kwargs):
        if self.is_active:
            WeeklyVideo.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_youtube_id(self):
            """
            Robustly extracts the video ID and removes hidden spaces.
            """
            import re
            if not self.video_url:
                return None
                
            # Regex for standard and short URLs
            regex = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
            
            match = re.search(regex, self.video_url)
            if match:
                # .strip() removes invisible spaces that cause Error 153
                return match.group(1).strip()
            return None

# 2. The Homepage Model
class HomePage(Page):    
    def get_context(self, request):
        context = super().get_context(request)
        # Fetch the one active video to show on the homepage
        context['active_video'] = WeeklyVideo.objects.filter(is_active=True).first()
        return context

class StandardPage(Page):
    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    body = RichTextField(blank=True)
    
    # Optional header image
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        FieldPanel('image'),
        FieldPanel('body'),
    ]