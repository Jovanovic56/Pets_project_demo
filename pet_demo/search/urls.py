from django.urls import path
from .views import search_pet

urlpatterns = [
    path('search/', search_pet, name='search_pet'),
]
