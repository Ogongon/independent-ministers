from django.http import JsonResponse
from .models import SpiritualSite

def site_list_api(request):
    sites = SpiritualSite.objects.all()
    data = []
    for site in sites:
        data.append({
            'name': site.name,
            'description': site.description,
            'lat': site.latitude,
            'lng': site.longitude,
            'photo_url': site.photo.url if site.photo else None,
        })
    

    return JsonResponse({'sites': data})