from django.urls import path
from . import views

app_name = 'medicine'

urlpatterns = [
    path('', views.index, name='index'),
    path('medicine/', views.index, name='search'),
    path('medicine/ingredient/', views.ingredient_search, name='ingredient'),
    path('medicine/company/', views.company_search, name='company'),
    path('medicine/efficacy/', views.efficacy_search, name='efficacy'),
    path('medicine/<int:pk>/', views.medicine_detail, name='detail'),
]
