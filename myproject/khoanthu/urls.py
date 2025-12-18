from django.urls import path
from . import views

urlpatterns = [
    path('', views.khoanthu, name='khoanthu'),
    path('create/', views.create_khoanthu, name='create_khoanthu'),
]
