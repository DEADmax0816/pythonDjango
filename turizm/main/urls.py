from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country-error', views.country_error, name='country-error'),
    path('countries', views.countries, name='countries')
]