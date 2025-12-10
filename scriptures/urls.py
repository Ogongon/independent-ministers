from django.urls import path
from . import views

urlpatterns = [
    path('texts/', views.comparison_list, name='ancient_texts'),
]