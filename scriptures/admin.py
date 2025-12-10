from django.contrib import admin
from .models import ScriptureComparison


@admin.register(ScriptureComparison)
class ScriptureComparisonAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'chapter', 'verse')
    search_fields = ('book_title', 'kjv_text', 'ethiopian_text')