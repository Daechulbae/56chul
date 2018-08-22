from django.urls import path
from . import views

app_name = 'Ali'
urlpatterns = [
    path('', views.index, name='action'),
    path('action/', views.status, name='actionaf'),
    path('forcoin/', views.forcoin, name='forcoin'),
]