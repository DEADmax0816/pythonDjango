from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country-error', views.country_error, name='country-error'),
    path('countries', views.countries, name='countries'),
    path('select', views.select, name='select'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('tables', views.tables, name='tables'),
    path('table_users', views.table_users, name='table_users'),
    path('table_tickets', views.table_tickets, name='table_tickets'),
]