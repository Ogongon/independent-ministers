from django.urls import path
from . import views

urlpatterns = [
    path('api/sites/', views.site_list_api, name='site_list_api'),
]