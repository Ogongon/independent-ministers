from django.shortcuts import render
from .models import ScriptureComparison

def comparison_list(request):
    comparisons = ScriptureComparison.objects.all().order_by('book_title', 'chapter', 'verse')
    context = {
        'comparisons': comparisons,
    }
    return render(request, 'scriptures/comparison_list.html', context)